import flet as ft
from main import *
import json
import re


def update_instruction_text(e: ft.ControlEvent):
    """
    Update the instruction text displayed in the GUI based on the current step in a pipeline.

    Parameters:
    - e (ft.ControlEvent): Control event triggering the update.

    Returns:
    - None
    """
    parameters, pipeline = parse_pipeline(e.page.data["steps_file_path"])

    current_step = get_step_name(e)

    instruction = build_instruction(pipeline, current_step, parameters)

    text_field = get_control(e, "full_instruction_text", data_mode=True)
    text_field.value = instruction[:-1]
    text_field.update()


def check_pipeline_context(page, pipeline, parameters):
    """
    Check the context of the pipeline for variable errors and display a message if errors are found.

    Parameters:
    - page: The page object where the pipeline is displayed.
    - pipeline: The pipeline dictionary containing step information.
    - parameters: The parameters dictionary used in the pipeline.

    Returns:
    - str: "Error" if variable errors are found, otherwise "Fine".
    """

    defined = set()
    error = False
    for step in pipeline:
        for in_out in pipeline[step]["with_var_inputs_outputs"]:
            defined.add(f"{step}.{in_out}")
        for param in parameters:
            defined.add(f"Parameters.{param}")
        for item in pipeline[step]:
            if item == "with_var_inputs_outputs":
                for text in pipeline[step][item].values():
                    vars = re.findall("@{(.+?)}", text)
                    for var in vars:
                        if var not in defined:
                            error = True

    if error == True:

        def close_bs(e: ft.ControlEvent):
            bs.open = False
            bs.update()

        bs = ft.BottomSheet(
            ft.Container(
                ft.Column(
                    [
                        ft.Text("Error. Check variables and steps order is correct."),
                        ft.ElevatedButton("Close", on_click=close_bs),
                    ],
                    tight=True,
                ),
                padding=10,
            ),
            open=True,
        )
        page.overlay.append(bs)
        page.update()

        return "Error"
    else:
        return "Fine"


def pipeline_to_file(page, pipeline, parameters):
    """
    Update the steps file with the pipeline information.

    Parameters:
    - page: The page object containing data and controls.
    - pipeline: Dictionary containing the pipeline steps and their details.
    - parameters: Dictionary of parameters used in the pipeline.

    Returns:
    - None
    """

    file_path = page.data["steps_file_path"]

    with open(file_path, "wt") as handle:
        handle.write("# Parameters\n")
        for el_key, el_val in parameters.items():
            handle.write(f"Parameters.{el_key} = {el_val}\n")
        handle.write("\n")
        for step in pipeline:
            handle.write(f"## {step}\n")
            handle.write(f'{step}.tool = {pipeline[step]["tool"]}\n')
            handle.write(f'{step}.tool_version = {pipeline[step]["tool_version"]}\n')
            handle.write(f'{step}.skip_loop = {pipeline[step]["skip_loop"]}\n')
            handle.write(f'{step}.delete_folder = {pipeline[step]["delete_folder"]}\n')
            handle.write("\n")
            for el_key, el_val in pipeline[step]["with_var_inputs_outputs"].items():
                handle.write(f"{step}.{el_key} = {el_val}\n")
            handle.write("\n")
            if pipeline[step]["with_var_command"] != "":
                text = pipeline[step]["with_var_command"]
                text = text.replace("\n", "@@n@@")
                handle.write(f"{step}.command = {text}\n\n")


def load_template_file(e):
    """
    Load a template file to be used in the pipeline.

    Parameters:
    - e (ft.ControlEvent): Control event triggering the function.

    Returns:
    - None
    """

    def on_dialog_result(e: ft.FilePickerResultEvent):
        if e.files != None:
            templates_file = e.files[0].path
            e.page.data["templates_file_path"] = templates_file

    file_picker = ft.FilePicker(on_result=on_dialog_result)
    e.page.overlay.append(file_picker)
    e.page.update()

    file_picker.pick_files(allow_multiple=False, initial_directory="/data/")


def save_step_template(e: ft.ControlEvent):
    def confirm_save_step(e: ft.ControlEvent, name):
        """
        Save the current step into the template file.

        Parameters:
        - e (ft.ControlEvent): Control event triggering the function.

        Returns:
        - None
        """

        try:
            templates_file = e.page.data["templates_file_path"]
            current_step = get_step_name(e)
            _, pipeline = parse_pipeline(e.page.data["steps_file_path"])

            with open(templates_file, "at") as handle:
                handle.write(f"## {name}\n")
                handle.write(f'{name}.tool = {pipeline[current_step]["tool"]}\n')
                if pipeline[current_step]["tool"] != "":
                    handle.write("\n")
                    for el_key, el_val in pipeline[current_step][
                        "with_var_inputs_outputs"
                    ].items():
                        handle.write(f"{name}.{el_key} = \n")
                    handle.write("\n")
                else:
                    handle.write("\n")
                    for el_key, el_val in pipeline[current_step][
                        "with_var_inputs_outputs"
                    ].items():
                        handle.write(f"{name}.{el_key} = \n")
                    handle.write("\n")
                    if pipeline[current_step]["with_var_command"] != "":
                        text = pipeline[current_step]["with_var_command"]
                        text = text.replace("\n", "@@n@@").replace(
                            current_step, "@@step_name@@"
                        )
                        handle.write(f"{name}.raw = {text}\n\n")

            out = f'Template ("{name}") saved succesfully at:\n {templates_file}'
        except KeyError:
            out = f'Template ("{name}") failed to save, templates file not loaded'

        def close_bs(e: ft.ControlEvent):
            bs.open = False
            bs.update()

        bs = ft.BottomSheet(
            ft.Container(
                ft.Column(
                    [ft.Text(out), ft.ElevatedButton("Close", on_click=close_bs)],
                    tight=True,
                ),
                padding=10,
            ),
            open=True,
        )
        e.page.overlay.append(bs)
        e.page.update()

    def close_dlg(e: ft.ControlEvent):
        if e.control.text == "Yes":
            name = get_control(e, "step_save_name_field", data_mode=True).value
            confirm_save_step(e, name)

        dlg.open = False
        e.page.update()

    name_field = ft.TextField(hint_text="Step name", data="step_save_name_field")

    dlg = ft.AlertDialog(
        modal=True,
        title=ft.Text("Write template text"),
        content=ft.Column([name_field]),
        actions=[
            ft.TextButton("No", on_click=close_dlg),
            ft.TextButton("Yes", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    e.page.dialog = dlg
    dlg.open = True
    e.page.update()


def load_step_template(e: ft.ControlEvent):
    """
    Loads a step template based on user interaction.

    Parameters:
    - e : ft.ControlEvent : Control event triggering the function

    Returns:
    - None
    """
    try:
        templates_file = e.page.data["templates_file_path"]
        _, saved_templates = parse_pipeline(templates_file)

        def close_dlg(e: ft.ControlEvent):
            _, saved_templates = parse_pipeline(
                templates_file, replace=name_field.value
            )
            parameters, pipeline = parse_pipeline(e.page.data["steps_file_path"])
            if e.control.text == "Yes":
                pipeline[name_field.value] = saved_templates[dropdown_templates.value]
                pipeline_to_file(e.page, pipeline, parameters)
                final_step = ft.TextButton(
                    text=name_field.value,
                    width=e.page.window_width / 5,
                    on_click=load_parameters,
                    key=f"Step_{name_field.value}_button",
                )
                steps_schema = get_control(e, "steps_schema", data_mode=True)
                steps_schema.controls.append(final_step)
                steps_schema.scroll_to(offset=-1)

            dlg.open = False
            e.page.update()

        name_field = ft.TextField(hint_text="Step name")
        dropdown_templates = ft.Dropdown(
            hint_text="Choose template",
            width=e.page.window_width / 7,
            options=[ft.dropdown.Option(i) for i in saved_templates.keys()],
        )

        dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text("Choose saved step"),
            content=ft.Column([name_field, dropdown_templates]),
            actions=[
                ft.TextButton("No", on_click=close_dlg),
                ft.TextButton("Yes", on_click=close_dlg),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        e.page.dialog = dlg
        dlg.open = True
        e.page.update()
    except KeyError:
        out = f"Failed to load templates, templates file not loaded"

        def close_bs(e: ft.ControlEvent):
            bs.open = False
            bs.update()

        bs = ft.BottomSheet(
            ft.Container(
                ft.Column(
                    [ft.Text(out), ft.ElevatedButton("Close", on_click=close_bs)],
                    tight=True,
                ),
                padding=10,
            ),
            open=True,
        )
        e.page.overlay.append(bs)
        e.page.update()


def get_control(e: ft.ControlEvent, key, data_mode=False):
    """
    Returns a control with the specified key

    Parameters:
    - e : ft.ControlEvent : Control event triggering the function
    - key : str : Key to search for in controls
    - data_mode : bool, optional : Flag to indicate data mode search

    Returns:
    - searched_el : Control : Control element with the specified key
    """
    for el, value in e.page.index.items():
        try:
            if data_mode == False:
                if value.key == key:
                    searched_el = e.page.get_control(el)
            else:
                if value.data == key:
                    searched_el = e.page.get_control(el)
        except AttributeError:
            pass

    return searched_el


def search_for_variables(text, current_step, pipeline, parameters):
    """
    Searches for variables in the pipeline and parameters based on the provided text. This is used for autocompletion in textfields.

    Parameters:
    - text : str : Text to search for in variables
    - current_step : str : Current step in the pipeline
    - pipeline : dict : Dictionary containing pipeline steps and variables
    - parameters : list : List of parameters

    Returns:
    - sorted(new_list) : list : List of variables matching the search text, sorted
    """
    defined = set()
    for step in pipeline:
        for in_out in pipeline[step]["with_var_inputs_outputs"]:
            defined.add(f"{step}.{in_out}")
        for param in parameters:
            defined.add(f"Parameters.{param}")
        if step == current_step:
            break

    new_list = list()
    for el in defined:
        if text in el:
            new_list.append(el)

    return sorted(new_list)


def find_pattern(text):
    """
    Finds the first element in the textfield with this regex pattern @{(?!.*}).*

    Parameters:
    - text : str : Text to search for the pattern

    Returns:
    - str or None : First element matching the pattern or None if not found
    """

    list_text = text.split(" ")
    for el in list_text:
        res = re.findall("@{(?!.*}).*", el)
        if len(res) >= 1:
            return res[0]

    return None


def replace_pattern(text, to_replace):
    """
    Replaces a specific pattern in the text with the provided replacement.

    Parameters:
    - text : str : Text containing patterns to be replaced
    - to_replace : str : String to replace the pattern with

    Returns:
    - str : Text with the pattern replaced
    """

    list_text = text.split(" ")
    final_text = ""
    done = False
    for el in list_text:
        res = re.findall("@{(?!.*}).*", el)
        if len(res) >= 1 and done == False:
            done = True
            el = el.replace(res[0], to_replace)
        final_text += el + " "

    return final_text


def add_reccomendations_to_col(e, col_data):
    """
    Adds recommendations to a column control based on user interactions.

    Parameters:
    - e : ft.ControlEvent : Control event triggering the function
    - col_data : str : Data related to the column control

    Returns:
    - None
    """

    def autocomplete(e: ft.ControlEvent):
        """
        Performs autocomplete functionality on a column control based on user input.

        Parameters:
        - e : ft.ControlEvent : Control event triggering the autocomplete
        - col_data : str : Data related to the column control

        Returns:
        - None
        """
        col = get_control(e, col_data, data_mode=True)
        if e.control.text != "...":
            col.controls[0].value = replace_pattern(
                col.controls[0].value, "@{" + e.control.text + "}"
            )

            if "input" in col_data or "output" in col_data:
                input_output = col_data.replace("_textfield_column", "")
                pipeline[get_step_name(e)]["with_var_inputs_outputs"][input_output] = (
                    col.controls[0].value
                )
            elif "command" in col_data:
                pipeline[get_step_name(e)]["with_var_command"] = col.controls[0].value

            pipeline_to_file(e.page, pipeline, parameters)
            col.controls = [col.controls[0]]
            update_instruction_text(e)
        else:
            search = search_for_variables(
                re.findall("@{(?!.*}).*", col.controls[0].value)[-1].replace("@{", ""),
                get_step_name(e),
                pipeline,
                parameters,
            )
            col.controls = [col.controls[0]]
            col.controls.append(
                ft.Row(
                    [
                        ft.TextButton(i, width=w / 6, on_click=autocomplete)
                        for i in search
                    ],
                    width=w / 1.5,
                    wrap=True,
                )
            )
        col.update()

    col = get_control(e, col_data, data_mode=True)
    w = e.page.window_width
    col.controls = [col.controls[0]]
    parameters, pipeline = parse_pipeline(e.page.data["steps_file_path"])
    if len(e.control.value) > 1:
        pattern_in_text = find_pattern(e.control.value)
        if pattern_in_text != None:
            search = search_for_variables(
                pattern_in_text.replace("@{", ""),
                get_step_name(e),
                pipeline,
                parameters,
            )
            if len(search) > 9:
                search = search[:8] + ["..."]
            col.controls.append(
                ft.Row(
                    [
                        ft.TextButton(i, width=w / 6.5, on_click=autocomplete)
                        for i in search
                    ],
                    width=e.control.width,
                    wrap=True,
                )
            )
        else:
            col.controls = [col.controls[0]]
    col.update()
    update_instruction_text(e)


def create_input_output_row(text1, text2, w, disabled=False):
    """
    Returns a row used in the inputs/outputs section.

    Parameters:
    - text1 : str : Text for the input/output row
    - text2 : str : Text for the custom text field
    - w : int : Width of the row
    - disabled : bool, optional : Flag to indicate if the row is disabled

    Returns:
    - parameter_row : Row : Row control for inputs/outputs
    """

    def update_inputs_outputs(e: ft.ControlEvent):
        """
        Updates the inputs or outputs based on user interaction.

        Parameters:
        - e : ft.ControlEvent : Control event triggering the update

        Returns:
        - None
        """
        to_update = e.control.data.split(".")[0]
        parameters, pipeline = parse_pipeline(e.page.data["steps_file_path"])
        step = get_step_name(e)
        pipeline[step]["with_var_inputs_outputs"][to_update] = e.data

        pipeline_to_file(e.page, pipeline, parameters)

        add_reccomendations_to_col(e, f"{text1}_textfield_column")

        update_instruction_text(e)

    def create_custom_textfield():
        """
        Creates a custom text field control.

        Returns:
        - field : Column : Column control containing the custom text field
        """
        field = ft.Column(
            [
                ft.TextField(
                    width=w / 2,
                    value=text2,
                    content_padding=0,
                    prefix_text="  ",
                    height=40,
                    disabled=disabled,
                    data=f"{text1}.textfield",
                    on_change=update_inputs_outputs,
                )
            ],
            data=f"{text1}_textfield_column",
        )
        return field

    def delete_input(e: ft.ControlEvent):
        """
        Deletes an input based on user interaction and updates the pipeline accordingly.

        Parameters:
        - e : ft.ControlEvent : Control event triggering the deletion

        Returns:
        - None
        """

        def del_in_out_update_pipeline(pipeline, to_delete):
            """
            Updates the pipeline by deleting a specific input/output and modifying related references.

            Parameters:
            - pipeline : dict : Dictionary representing the pipeline
            - to_delete : str : Element to be deleted in the format "step.variable"

            Returns:
            - pipeline : dict : Updated pipeline after the deletion
            """
            del_step, del_val = to_delete.split(".")
            pipeline[del_step]["with_var_inputs_outputs"].pop(del_val)

            ## remove the deleted inputs from other proccesses
            for step, info in pipeline.items():
                for item in info:
                    if item == "with_var_inputs_outputs":
                        for element, value in pipeline[step][item].items():
                            pipeline[step][item][element] = value.replace(to_delete, "")
                    elif item == "with_var_command":
                        pipeline[step][item] = pipeline[step][item].replace(
                            to_delete, ""
                        )

            ## rename the inputs or outputs in the step
            cat, number = del_val.split("_")
            new_values = dict()
            changed = dict()
            for element, value in pipeline[del_step]["with_var_inputs_outputs"].items():
                if cat in element:
                    c_num = int(element.split("_")[1])
                    if c_num > int(number):
                        new_values[f"{cat}_{c_num-1}"] = value
                        changed[element] = f"{cat}_{c_num-1}"
                    else:
                        new_values[element] = value
                else:
                    new_values[element] = value
            pipeline[del_step]["with_var_inputs_outputs"] = new_values

            ## rename that inputs or outputs whenever they are used on other steps

            for old, new in changed.items():
                for step, info in pipeline.items():
                    for item in info:
                        if item == "with_var_inputs_outputs":
                            for element, value in pipeline[step][item].items():
                                pipeline[step][item][element] = value.replace(old, new)
                        elif item == "with_var_command":
                            pipeline[step][item] = pipeline[step][item].replace(
                                old, new
                            )

            return pipeline

        to_delete = f"{get_step_name(e)}.{e.control.data.split('.')[0]}"
        parameters, pipeline = parse_pipeline(e.page.data["steps_file_path"])

        pipeline = del_in_out_update_pipeline(pipeline, to_delete)

        if check_pipeline_context(e.page, pipeline, parameters) != "Error":
            pipeline_to_file(e.page, pipeline, parameters)
            load_parameters(e, get_step_name(e))

        update_instruction_text(e)

    if text1 == "" and text2 == "":
        parameter_row = ft.Row()
    else:
        parameter_row = ft.Row(
            controls=[
                ft.Container(
                    content=ft.Text(
                        text1,
                        theme_style=ft.TextThemeStyle.BODY_LARGE,
                        text_align="center",
                    ),
                    alignment=ft.alignment.center,
                    width=w / 7,
                    height=40,
                    border_radius=4,
                ),
                create_custom_textfield(),
                ft.IconButton(
                    ft.icons.DELETE,
                    disabled=disabled,
                    on_click=delete_input,
                    data=f"{text1}.del_button",
                ),
            ],
            spacing=5,
            data=f"{text1}.row",
        )

    return parameter_row


def get_step_name(e):
    """
    Retrieves the name of the selected step.

    Parameters:
    - e : ControlEvent : Control event object

    Returns:
    - current_step_name : str : Name of the selected step
    """
    for control in e.page.index.values():
        if control.data == "ENABLED":
            current_step_name = control.text

    return current_step_name


def create_parameters_row(w, parameter, info=""):
    """
    Creates a row for setting parameters based on the parameter type.

    Parameters:
    - w : int : Width of the row
    - parameter : str : Type of parameter
    - info : str, optional : Additional information for the parameter

    Returns:
    - row : Row : Row control for setting parameters
    """

    def update_parameters(e: ft.ControlEvent):
        """
        Updates parameters based on user input and modifies the pipeline accordingly.

        Parameters:
        - e : ft.ControlEvent : Control event triggering the parameter update

        Returns:
        - None
        """
        parameters, pipeline = parse_pipeline(e.page.data["steps_file_path"])
        step = get_step_name(e)
        if parameter == "command":
            pipeline[step]["with_var_command"] = e.data

        pipeline_to_file(e.page, pipeline, parameters)

        if parameter == "command":
            add_reccomendations_to_col(e, f"{parameter}.textfield_row")

        update_instruction_text(e)

    if parameter == "command":
        row = ft.Row(
            [
                ft.Column(
                    [
                        ft.TextField(
                            value=info,
                            hint_text="Command",
                            width=w / 1.5,
                            content_padding=5,
                            prefix_text="  ",
                            on_change=update_parameters,
                            data=f"{parameter}.textfield",
                            multiline=True,
                        )
                    ],
                    data=f"{parameter}.textfield_row",
                )
            ],
            spacing=5,
        )
    else:
        row = ft.Row(
            [
                ft.Container(
                    content=ft.Text(
                        parameter,
                        theme_style=ft.TextThemeStyle.BODY_LARGE,
                        text_align="center",
                    ),
                    alignment=ft.alignment.center,
                    width=w / 7,
                    height=40,
                    border_radius=4,
                ),
                ft.TextField(
                    value=info,
                    hint_text=f"{parameter} value",
                    width=w / 5,
                    height=40,
                    content_padding=0,
                    prefix_text="  ",
                    on_change=update_parameters,
                    data=f"{parameter}.textfield",
                ),
            ],
            spacing=5,
        )
    return row


def upload_parameters(e: ft.ControlEvent):
    """
    Creates the parameters section based on the selected tool.

    Parameters:
    - e: a ControlEvent object representing the event triggering the function

    Returns:
    - None
    """

    tool = e.control.value.split(" (")[0]
    w = e.page.window_width

    parameter_col = get_control(e, "parameters_raw")
    parameters_raw_text = get_control(e, "parameters_raw_text")

    parameter_col.controls = list()

    parameter_col.controls.append(create_parameters_row(w, "command"))

    parameter_col.update()

    step = get_step_name(e)

    parameters, pipeline = parse_pipeline(e.page.data["steps_file_path"])

    if tool != "Custom":
        pipeline[step]["tool"] = tool
        parameters_raw_text.value = "PARAMETERS"
    else:
        parameters_raw_text.value = "RAW COMMAND"
        pipeline[step]["tool"] = ""

    parameters_raw_text.update()

    pipeline_to_file(e.page, pipeline, parameters)

    update_instruction_text(e)


def create_tools_menu(tools, w, key, disabled=False):
    """
    Creates a dropdown menu for selecting tools.

    Parameters:
    - tools: a list of tools to populate the dropdown menu
    - w: width parameter for the dropdown menu
    - key: key parameter for the dropdown menu
    - disabled: a boolean indicating if the dropdown should be disabled (default is False)

    Returns:
    - ft.Dropdown: a Dropdown object representing the created dropdown menu
    """
    tools = sorted(tools)
    tools.insert(0, "Custom")
    with open("scripts/tools_compatibility.json", "rt") as handle:
        compatibility = json.load(handle)
        compatibility["Custom"] = ""

    dropdown = ft.Dropdown(
        width=w / 5,
        height=47,
        options=[ft.dropdown.Option(f"{i}{compatibility[i]}") for i in tools],
        on_change=upload_parameters,
        key=key,
        disabled=disabled,
        content_padding=0,
        prefix_text="  ",
    )

    return dropdown


def load_parameters(e: ft.ControlEvent, custom_step=""):
    """
    Reads the current pipeline and displays the parameters for the selected option in the GUI.

    Parameters:
    - e: a ControlEvent object representing the event triggering the function
    - custom_step: a string representing a custom step (default is an empty string)

    Returns:
    - None
    """

    w = e.page.window_width
    _, pipeline = parse_pipeline(e.page.data["steps_file_path"])

    # activate buttons
    for el in [
        "tool_menu",
        "add_input_button",
        "add_output_button",
        "move_step_up",
        "move_step_down",
        "delete_step",
        "help_button_tool",
        "skip_loop_button",
        "help_button_docker_image",
        "delete_folder_button",
    ]:
        button = get_control(e, el)
        if el == "help_button_docker_image":
            button.icon_color = ft.colors.RED_500
        elif el == "help_button_tool":
            button.icon_color = ft.colors.BLUE_500
        button.disabled = False
        button.update()

    button = get_control(e, "tool_version_field", data_mode=True)
    button.disabled = False
    button.update()

    # disables the prior step before changing to the new one
    for control in e.page.index.values():
        if control.data == "ENABLED":
            control.style = ft.ButtonStyle()
            control.data = None
            control.update()

    if custom_step == "":
        step = e.control.text
        e.control.data = "ENABLED"  ## save in data that it is the current step
        e.control.style = ft.ButtonStyle(bgcolor=ft.colors.GREY_400)
        e.control.update()
    else:  # this loads the parameters of a defined step (not the one being clicked, which is the default behaviour)
        step = custom_step
        step_button = get_control(e, f"Step_{step}_button")
        step_button.data = "ENABLED"
        step_button.style = ft.ButtonStyle(bgcolor=ft.colors.GREY_400)
        step_button.update()

    inputs_outputs = pipeline[step]["with_var_inputs_outputs"]

    tool = pipeline[step]["tool"]
    tool_display = get_control(e, "tool_menu")

    inputs_col = get_control(e, "input_files")
    outputs_col = get_control(e, "output_files")
    parameters_col = get_control(e, "parameters_raw")
    parameters_raw_text = get_control(e, "parameters_raw_text")
    skip_loop_check = get_control(e, "skip_loop_button")
    delete_folder_check = get_control(e, "delete_folder_button")
    tool_version_field = get_control(e, "tool_version_field", data_mode=True)

    tool_version_field.value = pipeline[step]["tool_version"]
    delete_folder_check.value = pipeline[step]["delete_folder"]
    skip_loop_check.value = pipeline[step]["skip_loop"]

    inputs_col.controls = list()
    outputs_col.controls = list()
    parameters_col.controls = list()

    with open("scripts/tools_compatibility.json", "rt") as handle:
        compatibility = json.load(handle)
        compatibility["Custom"] = ""

    if tool in compatibility.keys():
        tool_display.value = f"{tool}{compatibility[tool]}"
        parameters_raw_text.value = "PARAMETERS"
    else:
        tool_display.value = "Custom"
        parameters_raw_text.value = "CUSTOM COMMAND"
        parameters_col.controls.append(
            create_parameters_row(w, "command", pipeline[step]["with_var_command"])
        )

    for key, in_out in inputs_outputs.items():
        if "input" in key:
            inputs_col.controls.append(create_input_output_row(key, in_out, w))
        elif "output" in key:
            outputs_col.controls.append(create_input_output_row(key, in_out, w))

    if tool != "":
        parameters_col.controls.append(
            create_parameters_row(w, "command", info=pipeline[step]["with_var_command"])
        )

    ## upload modified controls
    delete_folder_check.update()
    parameters_raw_text.update()
    tool_display.update()
    inputs_col.update()
    outputs_col.update()
    parameters_col.update()
    skip_loop_check.update()
    tool_version_field.update()
    update_instruction_text(e)


def generate_schema_buttons(w, pipeline):
    """
    Generates the schema for the entire pipeline and displays it in the GUI.

    Parameters:
    - w: width parameter for the schema buttons
    - pipeline: a dictionary representing the pipeline steps

    Returns:
    - ft.Column: a Column object containing the schema buttons for each step
    """

    # inside schema buttons controls goes all the steps in the pipeline
    # their width must be w/5
    steps = list(pipeline.keys())
    schema_buttons = ft.Column(
        controls=[
            ft.TextButton(
                text=i,
                width=w / 5,
                on_click=lambda x: load_parameters(x),
                key=f"Step_{i}_button",
            )
            for i in steps
        ],
        scroll=ft.ScrollMode.ALWAYS,
        data="steps_schema",
    )

    return schema_buttons


def page_resize(e: ft.ControlEvent, pipeline):
    """
    Resize elements in the GUI when the window width changes.

    Parameters:
    - e: a ControlEvent object representing the event triggering the function
    - pipeline: a dictionary representing the pipeline steps

    Returns:
    - None
    """

    if "steps_file_path" in e.page.data:
        _, pipeline = parse_pipeline(e.page.data["steps_file_path"])
        e.page.controls[1].controls[0].controls[0] = generate_schema_buttons(
            e.page.window_width, pipeline
        )
    e.page.controls[1].controls[2] = generate_step_info(e.page.window_width)
    e.page.update()


def append_element(e: ft.ControlEvent):
    """
    Appends an input or output element to the GUI based on the button clicked.

    Parameters:
    - e: a ControlEvent object representing the event triggering the function

    Returns:
    - None
    """

    button = e.control.key
    w = e.page.window_width
    parameters, pipeline = parse_pipeline(e.page.data["steps_file_path"])
    current_step = get_step_name(e)
    if button == "add_input_button":
        col = get_control(e, "input_files")
        num = len(col.controls) + 1
        col.controls.append(create_input_output_row(f"input_{num}", "", w))
        pipeline[current_step]["with_var_inputs_outputs"][f"input_{num}"] = ""
    elif button == "add_output_button":
        col = get_control(e, "output_files")
        num = len(col.controls) + 1
        col.controls.append(create_input_output_row(f"output_{num}", "", w))
        pipeline[current_step]["with_var_inputs_outputs"][f"output_{num}"] = ""
    pipeline_to_file(e.page, pipeline, parameters)
    col.update()
    update_instruction_text(e)


def delete_step_folders(e: ft.ControlEvent):
    """ 
    Updates the delete_folder status for the current step in the pipeline configuration. 
    
    Parameters: 
    - e : ft.ControlEvent object representing the event triggering the function 
    
    Returns: 
    - None 
    """ 
    current_step = get_step_name(e)
    parameters, pipeline = parse_pipeline(e.page.data["steps_file_path"])

    pipeline[current_step]["delete_folder"] = e.control.value

    pipeline_to_file(e.page, pipeline, parameters)


def generate_step_info(w):
    """
    Creates the base structure of the parameters section in the app for further updates.

    Parameters:
    - w: width parameter for the step information

    Returns:
    - ft.Column: a Column object representing the step information section
    """

    def open_help(e: ft.ControlEvent):
        """
        Opens the relevant help URL based on the current tool selection in the GUI.

        Parameters:
        - e: a ControlEvent object representing the event triggering the function

        Returns:
        - None
        """

        current_tool = get_control(e, "tool_menu").value.split("(")[0].strip()

        with open("scripts/tools_help.json", "rt") as handle:
            help = json.load(handle)
            help["Custom"] = ""

        with open("scripts/tools_compatibility.json", "rt") as handle:
            compatibility = json.load(handle)
            compatibility["Custom"] = ""

        if current_tool != "Custom":
            if "tool" in e.control.key:
                e.page.launch_url(help["urls_tools"][f"{current_tool}"])
            else:
                e.page.launch_url(help["urls_docker_images"][f"{current_tool}"])

    def skip_loop_action(e: ft.ControlEvent):
        """ 
        Updates the skip_loop status for the current step in the pipeline configuration based on the control event value. 

        Parameters: 
        - e : ft.ControlEvent object representing the event triggering the function 

        Returns: 
        - None 
        """ 
        current_step = get_step_name(e)
        parameters, pipeline = parse_pipeline(e.page.data["steps_file_path"])
        if e.control.value == True:
            pipeline[current_step]["skip_loop"] = True
        elif e.control.value == False:
            pipeline[current_step]["skip_loop"] = False

        pipeline_to_file(e.page, pipeline, parameters)

    def version_action(e: ft.ControlEvent):
        """ 
        Updates the tool version for the current step in the pipeline configuration based on the control event value. 

        Parameters: 
        - e : ft.ControlEvent object representing the event triggering the function 

        Returns: 
        - None 
        """ 
        current_step = get_step_name(e)
        parameters, pipeline = parse_pipeline(e.page.data["steps_file_path"])
        pipeline[current_step]["tool_version"] = e.control.value

        pipeline_to_file(e.page, pipeline, parameters)

    with open("scripts/tools_compatibility.json", "rt") as handle:
        tools_compatibility = json.load(handle)
        tools_compatibility["Custom"] = ""
    step_info = ft.Column(
        [
            ft.Column(
                controls=[
                    ft.Row(
                        [
                            ft.Row(
                                controls=[
                                    ft.Text("TOOL"),
                                    create_tools_menu(
                                        list(tools_compatibility.keys()),
                                        w,
                                        key="tool_menu",
                                        disabled=True,
                                    ),
                                    ft.TextField(
                                        value="latest",
                                        tooltip="Docker image version",
                                        width=w / 9,
                                        expand_loose=True,
                                        content_padding=0,
                                        prefix_text="  ",
                                        disabled=True,
                                        on_change=version_action,
                                        data=f"tool_version_field",
                                    ),
                                    ft.IconButton(
                                        icon=ft.icons.HELP,
                                        disabled=True,
                                        on_click=open_help,
                                        key="help_button_tool",
                                        tooltip="Tool help",
                                    ),
                                    ft.IconButton(
                                        icon=ft.icons.HELP,
                                        disabled=True,
                                        on_click=open_help,
                                        tooltip="Docker image help",
                                        key="help_button_docker_image",
                                    ),
                                ],
                                spacing=20,
                                data="tool_menu_row",
                            ),
                            ft.Row(
                                [
                                    ft.Checkbox(
                                        key="delete_folder_button",
                                        disabled=True,
                                        on_change=delete_step_folders,
                                    ),
                                    ft.Text("Delete step folders"),
                                    ft.Checkbox(
                                        key="skip_loop_button",
                                        disabled=True,
                                        on_change=skip_loop_action,
                                    ),
                                    ft.Text("Skip loop"),
                                ]
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Row(
                        controls=[
                            ft.Text("INPUTS"),
                            ft.IconButton(
                                ft.icons.ADD,
                                disabled=True,
                                key="add_input_button",
                                on_click=append_element,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Column(
                        controls=[create_input_output_row("", "", w, disabled=True)],
                        key="input_files",
                    ),
                    ft.Row(
                        controls=[
                            ft.Text("OUTPUTS"),
                            ft.IconButton(
                                ft.icons.ADD,
                                disabled=True,
                                key="add_output_button",
                                on_click=append_element,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Column(
                        controls=[create_input_output_row("", "", w, disabled=True)],
                        key="output_files",
                    ),
                    ft.Row(
                        controls=[
                            ft.Text("PARAMETERS", key="parameters_raw_text"),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Column(
                        controls=[create_input_output_row("", "", w, disabled=True)],
                        key="parameters_raw",
                    ),
                ],
                scroll=ft.ScrollMode.ALWAYS,
                expand=4,
            ),
            ft.Container(
                ft.Text(
                    value="",
                    data="full_instruction_text",
                    theme_style=ft.TextThemeStyle.TITLE_SMALL,
                    selectable=True,
                ),
                border=ft.border.all(1, ft.colors.BLACK),
                border_radius=4,
                padding=10,
                expand=1,
                alignment=ft.alignment.center_left,
            ),
        ],
        expand=3,
        spacing=1,
    )

    return step_info


def load_pipeline(e: ft.ControlEvent):
    ## Rewrite the update part
    """
    Reads the steps file and triggers the generation of schema buttons in the GUI.

    Parameters:
    - e: a ControlEvent object representing the event triggering the function

    Returns:
    - None
    """

    def on_dialog_result(e: ft.FilePickerResultEvent):
        """
        Handles the result of the file picker dialog, updating the GUI with the selected file's pipeline information.

        Parameters:
        - e: a FilePickerResultEvent object representing the file picker dialog result

        Returns:
        - None
        """
        if e.files != None:
            button = get_control(e, "add_step_button")
            button.disabled = False

            steps = e.files[0].path

            try:
                e.page.data["steps_file_path"] = steps
                _, pipeline = parse_pipeline(steps)
                e.page.controls[1].controls[0].controls[0] = generate_schema_buttons(
                    e.page.window_width, pipeline
                )
                e.page.controls[1].controls[2] = generate_step_info(e.page.window_width)
                e.page.update()
                error = False
            except:
                error = True

            def close_bs(e: ft.ControlEvent):
                bs.open = False
                bs.update()

            if error == False:

                out = "Pipeline Loaded!"
            else:
                out = "Error: Pipeline file is not correct."

            bs = ft.BottomSheet(
                ft.Container(
                    ft.Column(
                        [
                            ft.Text(out),
                            ft.ElevatedButton("Close", on_click=close_bs),
                        ],
                        tight=True,
                    ),
                    padding=10,
                ),
                open=True,
            )
            e.page.overlay.append(bs)
            e.page.update()

    file_picker = ft.FilePicker(on_result=on_dialog_result)
    e.page.overlay.append(file_picker)

    e.page.update()

    file_picker.pick_files(allow_multiple=False, initial_directory="/data/")


def create_new_project(e: ft.ControlEvent):
    """
    Creates a new project when the new project button is pressed.

    Parameters:
    - e: a ControlEvent object representing the event triggering the function

    Returns:
    - None
    """

    def on_dialog_result(e: ft.FilePickerResultEvent):
        """
        Handles the result of the file picker dialog, creating necessary files and updating the project path in the page data.

        Parameters:
        - e: a FilePickerResultEvent object representing the file picker dialog result

        Returns:
        - None
        """
        folder = e.path
        if folder != None:
            steps_intro = (
                "Parameters.filename = $filename\nParameters.base_dir = $HOST_PATH\n"
            )

            steps = f"{folder}/steps"
            input_filenames = f"{folder}/input_filenames.txt"
            with open(steps, "wt") as handle:
                handle.write(steps_intro)
            with open(input_filenames, "wt") as handle:
                handle.write("")

            e.page.data = {"steps_file_path": steps}
            e.page.data["inputs_file_path"] = input_filenames

    file_picker = ft.FilePicker(on_result=on_dialog_result)
    e.page.overlay.append(file_picker)
    e.page.update()
    file_picker.get_directory_path(initial_directory="/data/")


def add_step(e: ft.ControlEvent):
    """
    Controls the add step button functionality.

    Parameters:
    - e: a ControlEvent object representing the event triggered by the button

    Returns:
    - None
    """

    def confirm_step(e: ft.ControlEvent):
        """
        Confirms the addition of a step in the pipeline, updating the pipeline data and GUI accordingly.

        Parameters:
        - e: a ControlEvent object representing the event triggered by confirming the step

        Returns:
        - None
        """
        steps_schema = get_control(e, "steps_schema", data_mode=True)
        step_name = steps_schema.controls[0].content.value
        if step_name != "":
            parameters, pipeline = parse_pipeline(e.page.data["steps_file_path"])

            pipeline[step_name] = {
                "delete_folder": False,
                "skip_loop": False,
                "tool": str(),
                "tool_version": str(),
                "inputs_outputs": dict(),
                "with_var_inputs_outputs": dict(),
                "command": str(),
                "with_var_command": str(),
            }
            pipeline_to_file(e.page, pipeline, parameters)

            final_step = ft.TextButton(
                text=step_name,
                width=e.page.window_width / 5,
                on_click=lambda x: load_parameters(x),
                key=f"Step_{step_name}_button",
            )

            steps_schema.controls.append(final_step)
            steps_schema.controls.pop(0)
            steps_schema.scroll_to(offset=-1)
            steps_schema.update()

    steps_info = get_control(e, "steps_schema", data_mode=True)
    w = e.page.window_width
    temporary_step = ft.Container(
        ft.TextField(
            hint_text="Step name + ENTER",
            width=w / 6,
            height=50,
            content_padding=0,
            prefix_text="  ",
            on_submit=confirm_step,
        )
    )
    steps_info.controls.insert(0, temporary_step)
    steps_info.scroll_to(offset=0)
    steps_info.update()


def sort_pipeline(e: ft.ControlEvent):
    """
    Controls the functionality of moving steps up or down in the pipeline.

    Parameters:
    - e: a ControlEvent object representing the event triggered by the move step up/down buttons

    Returns:
    - None
    """

    parameters, pipeline = parse_pipeline(e.page.data["steps_file_path"])
    current_step_name = get_step_name(e)
    order = list(pipeline.keys())
    current_index = order.index(current_step_name)
    order.remove(current_step_name)
    if e.control.icon == ft.icons.MOVE_DOWN:
        new_index = current_index + 1
    elif e.control.icon == ft.icons.MOVE_UP:
        new_index = current_index - 1
    if new_index > len(pipeline) or new_index < 0:
        return pipeline
    order.insert(new_index, current_step_name)
    new_pipeline = dict()
    for step in order:
        new_pipeline[step] = pipeline[step]
    if check_pipeline_context(e.page, new_pipeline, parameters) != "Error":
        pipeline_to_file(e.page, new_pipeline, parameters)
        schema = get_control(e, "full_schema", data_mode=True)
        schema.controls[0] = generate_schema_buttons(e.page.window_width, new_pipeline)
        schema.update()
        col = get_control(e, "steps_schema", data_mode=True)
        rel_pos = list(new_pipeline.keys()).index(current_step_name) / len(new_pipeline)
        col.scroll_to(offset=(e.page.window_height - 10) * rel_pos)
        load_parameters(e, custom_step=current_step_name)


def delete_step(e: ft.ControlEvent):
    """
    Controls the functionality of deleting a step from the pipeline.

    Parameters:
    - e: a ControlEvent object representing the event triggered by the delete step button

    Returns:
    - None
    """

    current_step = get_step_name(e)

    parameters, pipeline = parse_pipeline(e.page.data["steps_file_path"])
    pipeline.pop(current_step)

    schema = get_control(e, "full_schema", data_mode=True)

    if check_pipeline_context(e.page, pipeline, parameters) != "Error":
        pipeline_to_file(e.page, pipeline, parameters)
        schema.controls[0] = generate_schema_buttons(e.page.window_width, pipeline)

        e.page.controls[1].controls[2] = generate_step_info(e.page.window_width)
        e.page.update()


def build_filenames(e: ft.ControlEvent):
    """
    Builds a list of filenames from selected files using a file picker dialog.

    Parameters:
    - e: a ControlEvent object representing the event triggering the function

    Returns:
    - None
    """

    def get_filenames(e: ft.FilePickerResultEvent):
        """
        Processes selected files from a file picker dialog to extract filenames and write them to a text file.

        Parameters:
        - e: a FilePickerResultEvent object representing the result of the file picker dialog

        Returns:
        - None
        """
        if e.files != None:
            with open("data/input_filenames.txt", "wt") as handle:
                for file in e.files:
                    file = file.name
                    file_split = file.split(".")
                    if len(file_split) > 1:
                        extension = file_split[-1]
                        handle.write(file.replace(f".{extension}", "") + "\n")

    file_picker = ft.FilePicker(on_result=get_filenames)

    e.page.overlay.append(file_picker)

    e.page.update()

    file_picker.pick_files(allow_multiple=True, initial_directory="/data/")


def load_filenames(e: ft.ControlEvent):
    def get_file(e: ft.FilePickerResultEvent):
        """
        Processes selected files from a file picker dialog to load the inputs file.

        Parameters:
        - e: a FilePickerResultEvent object representing the result of the file picker dialog

        Returns:
        - None
        """
        parameters, _ = parse_pipeline(e.page.data["steps_file_path"])
        e.page.data["inputs_file_path"] = e.files[0].path.replace(
            "/data", parameters["base_dir"], 1
        )
        e.page.update()

    file_picker = ft.FilePicker(on_result=get_file)

    e.page.overlay.append(file_picker)

    e.page.update()

    file_picker.pick_files(allow_multiple=False, initial_directory="/data/")


def display_help(e: ft.ControlEvent):
    e.page.launch_url("https://github.com/pegi3s/dockerfiles/tree/master/ngs_pipeliner/manual.md")
    e.page.update()


def generate_sh(e: ft.ControlEvent):
    """
    Generates an execution file based on the provided input filenames and steps file path. The loop type is determined based on the control event value, either 'files' or 'steps'. The function also creates a BottomSheet with a message and a button to close it.

    Parameters:
    - e : ft.ControlEvent : The control event triggering the function.

    Returns:
    - None
    """
    error = False
    try:
        filenames_file = e.page.data["inputs_file_path"]
    except KeyError:
        error = True

    steps_file_path = e.page.data["steps_file_path"]

    # control del swith y en funcion del valor cambiar loop_type
    loop_type = (
        "files" if get_control(e, "Steps_loop_button").trailing == None else "steps"
    )

    def close_bs(e: ft.ControlEvent):
        bs.open = False
        bs.update()

    if error == False:
        create_execution_file(loop_type, filenames_file, steps_file_path)
        out = 'Execution file ("run.sh") generated'
    else:
        out = "Error: Input filenames are not defined. Load/create inputs file."
    bs = ft.BottomSheet(
        ft.Container(
            ft.Column(
                [
                    ft.Text(out),
                    ft.ElevatedButton("Close", on_click=close_bs),
                ],
                tight=True,
            ),
            padding=10,
        ),
        open=True,
    )
    e.page.overlay.append(bs)
    e.page.update()


def loop_change(e: ft.ControlEvent):
    """
    Changes the loop type based on the control event key. If the key is 'Files_loop_button', the loop type is set to 'steps' and vice versa. Updates the control elements with the new loop type and adds a check icon to the triggering control.

    Parameters:
    - e : ft.ControlEvent : The control event triggering the function.

    Returns:
    - None
    """
    if e.control.key == "Files_loop_button":
        control = get_control(e, "Steps_loop_button")
    elif e.control.key == "Steps_loop_button":
        control = get_control(e, "Files_loop_button")

    control.trailing = None
    e.control.trailing = ft.Icon(ft.icons.CHECK)

    control.update()
    e.control.update()


def main(page: ft.Page):
    """
    Main function of the app. It generates the page by calling all the other functions.

    Parameters:
    - page: an ft.Page object representing the main page of the app

    Returns:
    - None
    """

    page.title = "NGS_Pipeliner"
    page.theme_mode = "LIGHT"

    page.data = dict()
    pipeline = dict()

    menubar = ft.MenuBar(
        expand=True,
        controls=[
            ft.SubmenuButton(
                content=ft.Text("File"),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("New pipeline"), on_click=create_new_project
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Create inputs file"), on_click=build_filenames
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Load pipeline"), on_click=load_pipeline
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Load inputs file"), on_click=load_filenames
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Load templates"), on_click=load_template_file
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Save step template"),
                        on_click=save_step_template,
                    ),
                ],
            ),
            ft.SubmenuButton(
                content=ft.Text("Run"),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Generate execution file"), on_click=generate_sh
                    ),
                    ft.SubmenuButton(
                        content=ft.Text("Loop type"),
                        controls=[
                            ft.MenuItemButton(
                                content=ft.Text("Files"),
                                trailing=ft.Icon(ft.icons.CHECK),
                                key="Files_loop_button",
                                on_click=loop_change,
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Steps"),
                                key="Steps_loop_button",
                                on_click=loop_change,
                            ),
                        ],
                    ),
                ],
            ),
            ft.MenuItemButton(ft.Text("Help"), on_click=display_help),
        ],
    )

    schema_buttons = generate_schema_buttons(page.window_width, pipeline)

    schema_controls = ft.Column(
        controls=[
            ft.PopupMenuButton(
                icon=ft.icons.ADD,
                disabled=True,
                key="add_step_button",
                items=[
                    ft.PopupMenuItem(text="Add empty step", on_click=add_step),
                    ft.PopupMenuItem(
                        text="Add step from template", on_click=load_step_template
                    ),
                ],
            ),
            ft.IconButton(
                icon=ft.icons.DELETE,
                disabled=True,
                key="delete_step",
                on_click=delete_step,
            ),
            ft.IconButton(
                icon=ft.icons.MOVE_UP,
                disabled=True,
                key="move_step_up",
                on_click=sort_pipeline,
            ),
            ft.IconButton(
                icon=ft.icons.MOVE_DOWN,
                disabled=True,
                key="move_step_down",
                on_click=sort_pipeline,
            ),
        ]
    )

    schema = ft.Row(
        controls=[schema_buttons, schema_controls],
        expand=1,
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=ft.CrossAxisAlignment.START,
        data="full_schema",
    )

    step_info = generate_step_info(page.window_width)

    main_window = ft.Row(
        controls=[
            schema,
            ft.VerticalDivider(color=ft.colors.BLACK, thickness=1, visible=True),
            step_info,
        ],
        vertical_alignment=ft.CrossAxisAlignment.START,
        spacing=5,
        expand=True,
    )

    page.add(ft.Row([menubar]), main_window)

    page.on_resize = lambda x: page_resize(x, pipeline)

    page.update()


# Run the app
ft.app(main)
