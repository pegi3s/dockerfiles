# Building instructions

This image is not built anymore. Scipio is discontinued, so the repository metadata was
updated to reflect that and the image is only retagged when needed.

# Notes

Scipio is no longer maintained: version 1.4 was released in 2010 and version 1.4.1 in 2013
(13 years ago), and the project has had no activity since then. For this reason we consider
the project discontinued (`project_active: false` in the metadata) and we do not rebuild the
image.

The existing image already ships the 1.4.1 scripts (`scipio.1.4.1.pl`), so it was simply
retagged as `pegi3s/scipio:1.4.1` (and `:latest`) to match the actual scripts and to avoid the
updater checker reporting a non-existent update. The old `1.4` value has been moved to
`no_longer_tested`.

# Build log

- 1.4 - 21/12/2022 - Pedro Ferreira
