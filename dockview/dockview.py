#!/usr/bin/env python3
"""
Flags:
    -t SECONDS   Polling interval in seconds (default: 5)
    -o FILE      Output file path (default: docker_stats.txt)
"""

import argparse
import os
import signal
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

import docker


# ---------------------------------------------------------------------------
# Per-container accumulated statistics
# Key: container short ID
# Value: dict with name, image, sample count, running sums, min/max
# ---------------------------------------------------------------------------
stats_data: dict = {}


# ---------------------------------------------------------------------------
# Docker stats calculation helpers
# ---------------------------------------------------------------------------

def _cpu_percent(stats: dict) -> float:
    """Return CPU usage as a percentage across all available CPUs."""
    try:
        cpu_delta = (
            stats["cpu_stats"]["cpu_usage"]["total_usage"]
            - stats["precpu_stats"]["cpu_usage"]["total_usage"]
        )
        system_delta = (
            stats["cpu_stats"]["system_cpu_usage"]
            - stats["precpu_stats"]["system_cpu_usage"]
        )
        if system_delta <= 0 or cpu_delta < 0:
            return 0.0

        num_cpus = stats["cpu_stats"].get("online_cpus")
        if num_cpus is None:
            percpu = stats["cpu_stats"]["cpu_usage"].get("percpu_usage") or [1]
            num_cpus = len(percpu)

        return (cpu_delta / system_delta) * num_cpus * 100.0
    except (KeyError, ZeroDivisionError):
        return 0.0


def _mem_mb(stats: dict) -> float:
    """Return actual memory usage in MiB (cache excluded when available)."""
    mem = stats.get("memory_stats", {})
    usage = mem.get("usage", 0)
    # cgroup v1 exposes a 'cache' key inside 'stats'; subtract it for
    # the true working-set memory.  cgroup v2 already excludes page cache.
    cache = mem.get("stats", {}).get("cache", 0)
    return max(0.0, usage - cache) / (1024 * 1024)


# ---------------------------------------------------------------------------
# Stats accumulation
# ---------------------------------------------------------------------------

def _update(container_id: str, name: str, image: str, cpu: float, mem: float) -> None:
    if container_id not in stats_data:
        stats_data[container_id] = {
            "name": name,
            "image": image,
            "samples": 0,
            "cpu_sum": 0.0,
            "cpu_min": float("inf"),
            "cpu_max": float("-inf"),
            "mem_sum": 0.0,
            "mem_min": float("inf"),
            "mem_max": float("-inf"),
        }
    d = stats_data[container_id]
    d["samples"] += 1
    d["cpu_sum"] += cpu
    d["cpu_min"] = min(d["cpu_min"], cpu)
    d["cpu_max"] = max(d["cpu_max"], cpu)
    d["mem_sum"] += mem
    d["mem_min"] = min(d["mem_min"], mem)
    d["mem_max"] = max(d["mem_max"], mem)


# ---------------------------------------------------------------------------
# Output writer
# ---------------------------------------------------------------------------

def _write(output_file: str) -> None:
    """Overwrite the output file with current aggregated statistics."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = [
        "Docker Container Statistics",
        f"Last updated : {now}",
        "=" * 72,
        "",
    ]

    active = {cid: d for cid, d in stats_data.items() if d["samples"] > 0}

    if not active:
        lines.append("No container data collected yet.")
    else:
        for cid, d in active.items():
            cpu_avg = d["cpu_sum"] / d["samples"]
            mem_avg = d["mem_sum"] / d["samples"]
            lines += [
                f"Container : {d['name']}  [{cid[:12]}]",
                f"Image     : {d['image']}",
                f"Samples   : {d['samples']}",
                f"CPU usage :",
                f"  Average : {cpu_avg:8.2f} %",
                f"  Minimum : {d['cpu_min']:8.2f} %",
                f"  Maximum : {d['cpu_max']:8.2f} %",
                f"RAM usage :",
                f"  Average : {mem_avg:8.2f} MiB",
                f"  Minimum : {d['mem_min']:8.2f} MiB",
                f"  Maximum : {d['mem_max']:8.2f} MiB",
                "",
            ]

    with open(output_file, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))


# ---------------------------------------------------------------------------
# Per-container polling task (runs in thread pool)
# ---------------------------------------------------------------------------

def _poll_container(container) -> tuple | None:
    """Fetch a single container's stats; return (id, name, image, cpu%, mem_mb) or None."""
    try:
        raw = container.stats(stream=False)
        cpu = _cpu_percent(raw)
        mem = _mem_mb(raw)
        image_tags = container.image.tags
        image = image_tags[0] if image_tags else container.image.short_id
        return (container.id, container.name, image, cpu, mem)
    except Exception as exc:
        print(f"[warn] Could not get stats for {container.name}: {exc}", file=sys.stderr)
        return None


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    version = os.environ.get("DOCKVIEW_VERSION")
    if version:
        version_description = f" (version: {version})"
    else:
        version_description = ""

    parser = argparse.ArgumentParser(
        description=f"Monitor CPU and RAM usage of all running Docker containers{version_description}"
    )
    parser.add_argument(
        "-t",
        type=float,
        default=5.0,
        metavar="SECONDS",
        help="Polling interval in seconds (default: 5)",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="docker_stats.txt",
        metavar="FILE",
        help="Output file path (default: docker_stats.txt)",
    )
    args = parser.parse_args()

    try:
        client = docker.from_env()
        client.ping()
    except Exception as exc:
        sys.exit(f"Cannot connect to Docker daemon: {exc}")

    def _shutdown(signum, frame):
        print("\nShutting down — writing final stats …", file=sys.stderr)
        _write(args.output)
        sys.exit(0)

    signal.signal(signal.SIGINT, _shutdown)
    signal.signal(signal.SIGTERM, _shutdown)

    if version:
        print(f"Running dockview version: {version}", file=sys.stderr)

    print(
        f"Monitoring Docker containers  |  interval: {args.t}s  |  output: {args.output}",
        file=sys.stderr,
    )
    print("Press Ctrl+C to stop.\n", file=sys.stderr)

    while True:
        try:
            containers = client.containers.list()
        except Exception as exc:
            print(f"[error] Could not list containers: {exc}", file=sys.stderr)
            time.sleep(args.t)
            continue

        if containers:
            # Poll all containers in parallel to avoid blocking per-container
            with ThreadPoolExecutor(max_workers=min(len(containers), 16)) as pool:
                futures = {pool.submit(_poll_container, c): c for c in containers}
                for future in as_completed(futures):
                    result = future.result()
                    if result is not None:
                        _update(*result)

        _write(args.output)

        time.sleep(args.t)


if __name__ == "__main__":
    main()
