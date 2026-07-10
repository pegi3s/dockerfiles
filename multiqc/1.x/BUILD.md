 # Building instructions

 Run:

 ```bash
 multiqc_version=1.35 && docker build ./ -t pegi3s/multiqc:${multiqc_version} --build-arg VERSION=${multiqc_version} && docker tag pegi3s/multiqc:${multiqc_version} pegi3s/multiqc:latest
 ```

 # Build log

 - 1.35 - 09/07/2026 - Hugo López Fernández
