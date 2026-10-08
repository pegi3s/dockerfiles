# Building instructions

The image bundles both a wrapper script (whose version is stored in the `current.version` file)
and the `tmtools` Python package. The image version combines both:
`<script_version>_tmtools_<tmtools_version>`.

Specify the `tmtools` version in `tmtools_version` and run (from this `current/` directory):

```bash
script_version=$(cat current.version) && tmtools_version=0.3.0 && docker build ./ -t pegi3s/tmtools:${script_version}_tmtools_${tmtools_version} --build-arg VERSION=${tmtools_version} && docker tag pegi3s/tmtools:${script_version}_tmtools_${tmtools_version} pegi3s/tmtools:latest
```

# Notes

Earlier tags only referenced the wrapper script version (e.g. `1.0.1`), even though the image
also bundles the `tmtools` Python package. Since the `tmtools` package has its own versioning
(and the updater checker tracks it through the GitHub repository), the image version now
combines both: `<script_version>_tmtools_<tmtools_version>`.

The `tmtools` package is parametrized through the `VERSION` build argument, while `numpy` and
`biopython` are pinned directly in the `Dockerfile` (the `requirements.txt` file was removed)
to make the build fully reproducible. Note that, when `tmtools` is updated to a new version,
the pinned `numpy`/`biopython` versions may also need to be revisited.

The existing `1.0.1` image (which already bundled `tmtools 0.3.0`, `numpy 2.2.6` and
`biopython 1.86`) was retagged as `1.0.1_tmtools_0.3.0`. The previous files are kept in the
`old/` directory.

# Build log

- 1.0.1_tmtools_0.3.0 - 08/10/2026 - Hugo López Fernández
- 1.0.1 - 01/03/2026 - Hugo López Fernández
- 1.0.0 - Hugo López Fernández
