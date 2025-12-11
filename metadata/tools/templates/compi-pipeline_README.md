# {{tool_name}} [![license](https://img.shields.io/badge/license-MIT-brightgreen)]({{tool_license_url}}) [![dockerhub](https://img.shields.io/badge/hub-docker-blue)]({{tool_dockerhub_url}}) [![compihub](https://img.shields.io/badge/hub-compi-blue)]({{tool_compihub_url}})
> **{{tool_name}}** is {{tool_description}}. A Docker image is available in [this Docker Hub repository]({{tool_dockerhub_url}}).

## {{tool_name}} repositories

- [GitHub]({{tool_github_url}})
- [DockerHub]({{tool_dockerhub_url}})
- [CompiHub]({{tool_compihub_url}})

# What does {{tool_name}} do?

{{tool_long_description}}

This process comprises the following steps:

{{tool_steps}}

# Using the {{tool_name}} image in Linux

In order to use the {{tool_name}} image, create first a directory in your local file system (e.g. `{{project_directory_name}}`) with the following structure: 

```bash
{{project_directory_structure}}
```

Where:

{{project_directory_explanation}}

You can populate the project directory running the following command:
```bash
{{docker_init_command}}
```

Now, you should:

{{project_instructions}}

Once this structure and files are ready, you should run and adapt the following commands to run the entire pipeline:
```bash
{{docker_run_pipeline}}
```
