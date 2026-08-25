# Building instructions

Specify the TakeABreak version in `takeabreak_version` and run:

```bash
takeabreak_version=1.1.2 && docker build ./ -t pegi3s/takeabreak:${takeabreak_version} --build-arg VERSION=${takeabreak_version} && docker tag pegi3s/takeabreak:${takeabreak_version} pegi3s/takeabreak:latest
```

# Build log

- 1.1.2 - 25/08/2026 - Hugo López Fernandez
- 1.0.0 - 09/06/2022 - Pedro Ferreira
