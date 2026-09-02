#!/bin/bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

for test_script in "$SCRIPT_DIR"/test_*.sh; do
    echo "[test] Running $(basename "$test_script")"
    bash "$test_script"
done

echo "[test] All tests passed! :-D"