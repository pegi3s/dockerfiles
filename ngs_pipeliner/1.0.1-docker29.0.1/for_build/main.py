import os
import re
import json
import graphviz

###################################################################################################################################
# Tool instruction building
###################################################################################################################################


def build_instruction(pipeline, step, parameters):
    """
    Builds a Docker instruction based on the specified pipeline, step, and parameters.

    Parameters:
    - pipeline : dictionary containing the pipeline configuration
    - step : key indicating the specific step in the pipeline
    - parameters : dictionary containing the parameters for the pipeline execution

    Returns:
    - instruction : a Docker instruction generated based on the pipeline configuration
    """
    tool = pipeline[step]["tool"]
    version = pipeline[step]["tool_version"]

    with open("scripts/tools_images.json", "rt") as handle:
        images = json.load(handle)

    base_dir = parameters["base_dir"]

    try:
        if tool != "":
            command = parse_variants(pipeline[step]["command"], pipeline, parameters)
            if version == "latest":
                instruction = (
                    f"docker run --rm -v {base_dir}:/data {images[tool]} {command}"
                )
            else:
                instruction = f"docker run --rm -v {base_dir}:/data {images[tool]}:{version} {command}"
        else:
            instruction = parse_variants(
                pipeline[step]["command"], pipeline, parameters
            )
    except KeyError:
        instruction = ""

    return instruction + "\n"


###################################################################################################################################
# Utility functions
###################################################################################################################################


def parse_variants(text, pipeline, parameters):
    """
    This function replaces the referenced variables in the 'text' with corresponding values from the 'pipeline' and 'parameters'.

    Parameters:
    - text : the text containing referenced variables to be replaced
    - pipeline : dictionary containing the pipeline configuration
    - parameters : dictionary containing the parameters for the pipeline execution

    Returns:
    - modified_text : the text with replaced variables based on the pipeline and parameters
    """
    try:
        if parameters["filename"] == "":
            parameters["filename"] = "@{Parameters.filename}"
    except:
        pass

    vars = re.findall("@{(.+?)}", text)
    try:
        for var in vars:
            s, v = var.split(".")
            if s != "Parameters":
                text = text.replace(f"@{{{var}}}", pipeline[s]["inputs_outputs"][v])
            else:
                text = text.replace(f"@{{{var}}}", parameters[v])
    except:
        pass

    return text


def parse_pipeline(file_path, replace=None):
    """
    This function reads the steps file and parses the pipeline configuration.

    Parameters:
    - file_path : the path to the steps file to be read
    - replace : optional parameter for replacing a specific string in the file

    Returns:
    - parameters : dictionary containing the parameters extracted from the file
    - pipeline : dictionary containing the parsed pipeline configuration
    """
    parameters = dict()
    pipeline = dict()

    with open(file_path, "rt") as handle:
        for line in handle:
            if line[0] != "#" and line != "\n":
                line = line.replace("\n", "")
                line = line.split("=", maxsplit=1)
                step, value = line[0].split(".")
                step = step.strip()
                value = value.strip()
                line[1] = line[1].strip()
                if replace is not None:
                    line[1] = line[1].replace("@@step_name@@", replace)

                if step == "Parameters":
                    parameters[value] = line[1]
                    continue

                if step not in pipeline:
                    pipeline[step] = {
                        "delete_folder": False,
                        "skip_loop": False,
                        "tool": str(),
                        "tool_version": str(),
                        "inputs_outputs": dict(),
                        "with_var_inputs_outputs": dict(),
                        "command": str(),
                        "with_var_command": str(),
                    }

                if value == "tool":
                    pipeline[step]["tool"] = line[1]
                elif value == "skip_loop":
                    pipeline[step]["skip_loop"] = True if line[1] == "True" else False
                elif value == "tool_version":
                    pipeline[step]["tool_version"] = line[1]
                elif value == "delete_folder":
                    pipeline[step]["delete_folder"] = (
                        True if line[1] == "True" else False
                    )
                elif "input" in value or "output" in value:
                    pipeline[step]["with_var_inputs_outputs"][value] = line[1]
                    line[1] = parse_variants(line[1], pipeline, parameters)
                    pipeline[step]["inputs_outputs"][value] = line[1]
                elif value == "command":
                    pipeline[step]["with_var_command"] = line[1].replace("@@n@@", "\n")
                    line[1] = parse_variants(line[1], pipeline, parameters)
                    pipeline[step]["command"] = line[1].replace("@@n@@", "\n")

    for step in pipeline:
        if pipeline[step]["tool_version"] == str() and pipeline[step]["tool"] != str():
            pipeline[step]["tool_version"] = "latest"

    return parameters, pipeline


def check_ouput_folders(pipeline):
    """
    Checks if the output folders exist, and creates them if they do not.

    Parameters:
    - pipeline : dictionary containing the pipeline configuration

    Returns:
    - list of folders: a list of output folders that need to be created
    """

    folders2 = set()
    for step in pipeline:
        inputs_outputs = pipeline[step]["inputs_outputs"]
        for key, value in inputs_outputs.items():
            if "output" in key:
                if "/" in value:
                    folders = value.split("/")[:-1]
                path = "$HOST_PATH/"
                for folder in folders:
                    path += f"{folder}/"

                folders2.add(path)

    return list(folders2)


def generate_schematics(pipeline):
    """
    Generates a schematic representation of the pipeline using graphviz.

    Parameters:
    - pipeline : dictionary containing the pipeline configuration

    Returns:
    - None
    """
    schema = graphviz.Digraph(comment="Pipeline")
    schema.format = "png"
    schema.node("Input files", "Input files")
    for step in pipeline:
        schema.node(step, step)

    edges = set()
    for step in pipeline:
        inputs_outputs = pipeline[step]["with_var_inputs_outputs"]
        inputs = list()
        for el, val in inputs_outputs.items():
            if "input" in el:
                try:
                    input = (
                        re.findall("@{.*?}", val)[-1].replace("@{", "").replace("}", "")
                    )
                    inputs.append(input)
                except:
                    pass
        for el in inputs:
            if el == "Parameters.filename":
                edges.add(f"Input files>>>{step}")
            else:
                for step1 in pipeline:
                    if step1 == el.split(".")[0]:
                        edges.add(f"{step1}>>>{step}")

    for edge in edges:
        edge = edge.split(">>>")
        schema.edge(edge[0], edge[1])

    schema.format = "svg"
    schema.render("data/pipeline_schema", cleanup=True)
    schema.format = "png"
    schema.render("data/pipeline_schema", cleanup=True)


###################################################################################################################################
# Launch pipeline function
###################################################################################################################################


def create_execution_file(loop_type, filenames_file, step_file_path):
    """
    Creates an execution file based on the pipeline configuration and specified parameters.

    Parameters:
    - loop_type : type of loop for execution (either "files" or "steps")
    - filenames_file : path to the file containing filenames
    - step_file_path : path to the steps file for parsing pipeline configuration

    Returns:
    - None
    """
    parameters, pipeline = parse_pipeline(step_file_path)
    delete_at_step = dict()
    outputs_to_delete = dict()
    folders = check_ouput_folders(pipeline)
    for step in pipeline:
        delete_at_step[step] = []
        if pipeline[step]["delete_folder"] == True:
            for el in pipeline[step]["with_var_inputs_outputs"].keys():
                if "output" in el:
                    outputs_to_delete[f"{step}.{el}"] = None

    for el in outputs_to_delete:
        for step in pipeline:
            for key, val in pipeline[step]["with_var_inputs_outputs"].items():
                if f"@\u007b{el}\u007d" in val:
                    outputs_to_delete[el] = step

    try:
        for el, val in outputs_to_delete.items():
            if val is None:
                delete_at_step[list(pipeline.keys())[-1]].append(el)
            else:
                delete_at_step[val].append(el)
    except KeyError:
        pass

    with open("data/run.sh", "wt") as handle:
        handle.write(f"sed -i 's/\\r//' {filenames_file}\n")
        for folder in folders:
            handle.write(f"mkdir -p {folder}\n")
        if loop_type == "files":
            steps = list(pipeline.keys())
            skiped = True
            while len(steps) != 0:
                if pipeline[steps[0]]["skip_loop"] == False:
                    if skiped == False:
                        handle.write(f'echo "$filename {steps[0]}"\n')
                        instruction = build_instruction(pipeline, steps[0], parameters)
                        handle.write(instruction)
                    else:
                        handle.write(f"cat {filenames_file} | while read filename\n")
                        handle.write("do\n")
                        handle.write(f'echo "$filename {steps[0]}"\n')
                        instruction = build_instruction(pipeline, steps[0], parameters)
                        handle.write(instruction)

                    skiped = False
                else:
                    if skiped == False:
                        handle.write("done\n")

                    handle.write(f'echo "{steps[0]}"\n')
                    instruction = build_instruction(pipeline, steps[0], parameters)
                    handle.write(instruction)
                    skiped = True

                if len(delete_at_step[steps[0]]) != 0:
                    for el in delete_at_step[steps[0]]:
                        del_step, del_out = el.split(".")
                        handle.write(
                            f'rm -f {parse_variants(pipeline[del_step]["with_var_inputs_outputs"][del_out], pipeline, parameters)}\n'
                        )
                steps = steps[1:]
            if skiped == False:
                handle.write("done\n")
        elif loop_type == "steps":
            for step in pipeline:
                if pipeline[step]["skip_loop"] == False:
                    handle.write(f"cat {filenames_file} | while read filename\n")
                    handle.write("do\n")
                    handle.write(f'echo "$filename {step}"\n')
                    instruction = build_instruction(pipeline, step, parameters)
                    handle.write(instruction)
                    handle.write(f"done\n")
                else:
                    handle.write(f'echo "{step}"\n')
                    instruction = build_instruction(pipeline, step, parameters)
                    handle.write(instruction)

                for el in delete_at_step[step]:
                    del_step, del_out = el.split(".")
                    handle.write(f"cat {filenames_file} | while read filename\n")
                    handle.write("do\n")
                    handle.write(
                        f'rm -f {parse_variants(pipeline[del_step]["with_var_inputs_outputs"][del_out], pipeline, parameters)}\n'
                    )
                    handle.write(f"done\n")
        handle.write("find $HOST_PATH/ -empty -type d -delete\n")

    # Read in the file
    with open("data/run.sh", "r") as file:
        filedata = file.read()

    host_path = (
        os.getenv("HOST_PATH")
        if os.getenv("HOST_PATH")[-1] != "/"
        else os.getenv("HOST_PATH")[:-1]
    )

    # Replace the target string
    filedata = filedata.replace("$HOST_PATH", host_path)

    # Write the file out again
    with open("data/run.sh", "w") as file:
        file.write(filedata)

    # Generate schematics
    generate_schematics(pipeline)
