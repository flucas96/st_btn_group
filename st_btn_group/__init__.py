import streamlit.components.v1 as components
import os
import mimetypes

_RELEASE = True

if not _RELEASE:
    _component_func = components.declare_component(
        "st_btn_group",
        url="http://localhost:3000",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("st_btn_group", path=build_dir)

def create_download_function(file_data: str, file_name: str, file_mime_type: str = None) -> str:
    if not file_mime_type:
        file_mime_type, _ = mimetypes.guess_type(file_name)
    return f"""(function() {{
        const link = document.createElement('a');
        link.href = '{file_data}';
        link.download = '{file_name}';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }})()"""

def st_btn_group(buttons: list, group_style:dict={}, key:str = "first_carousel", return_value = True, shape:str="default",disabled:bool=False, size:str="default",
                 mode:str="default",theme:str="light", height:int=60, align:str="left"):
    
    """

    Parameters
    ----------
    key : str, optional 

    buttons: list of dict. example 
    [{"label": "<h1> Button 1</h1>","disabled":False, "value":"1", "onClick":"console.log('clicked')","startEnhancer":"<h1>Start</h1>",
    "endEnhancer":"<h1>Ende</h1>", style={"backgroundColor":"red", "download_file":{"data": "base64 encoded data", "filename": "filename", "mime_type": "mime_type (optional)"}}}}"]
        One Button is a dict that can have the following keys:
            label: str - The label of the button. You can use HTML tags to style the label or add fontawesome icons
            value: any - The value of the button. This value will be returned to Streamlit when the button is clicked
            disabled: bool - If True the button is disabled
            onClick: str - A JavaScript function that will be executed when the button is clicked
            startEnhancer: str - A HTML string that will be displayed before the label of the button (left side) - fontawesome icons are supported (example: <i class='fas fa-home'></i>)
            endEnhancer: str - A HTML string that will be displayed after the label of the button (right side) - fontawesome icons are supported (example: <i class='fas fa-home'></i>)
            style: dict - A dict with CSS properties that will be applied to the button

            download_file: dict - A dict with the following keys:
                data: str - base64 encoded data
                filename: str - filename (please add the file extension)
                mime_type: str - mime_type (optional) - if not provided the mime_type will be guessed from the filename

    
    
    group_style: dict, optional: default: {"marginTop": "4px","marginLeft": "4px","gap": "5px",}

    return_value: bool, optional - If False Streamlit wont receive any value from the component
    disabled: bool, optional - Disables the whole Button group

    shape: str, optional - default, pill, round, circle, square
    size: str, optional - default, large, compact, mini
    mode: str, optional - default, checkbox, radio

    theme: str, optional - light, dark

    height: int, optional - height of the button group
    align: str, optional - left, center, right
    """

    default_group_style = {
        "marginTop": "4px",
        "marginLeft": "4px",
        "gap": "5px",
    }

    for css_op in default_group_style:
        if css_op not in group_style:
            group_style[css_op] = default_group_style[css_op]

    div_id = f"btn_group_container_{key}"
    div_style = {}

    if align == "center":
        div_style["display"] = "flex"
        div_style["flexWrap"] = "wrap"
        div_style["justifyContent"] = "center"
        div_style["alignItems"] = "center"

    elif align == "right":
        div_style["position"] = "absolute"
        div_style["top"] = "0"
        div_style["right"] = "0"
    elif align == "left":
        div_style["position"] = "absolute"
        div_style["top"] = "0"
        div_style["left"] = "0"

    for button in buttons:
        if "download_file" in button:
            file_data = button["download_file"]["data"]
            file_mime_type = button["download_file"]["mime_type"] if "mime_type" in button["download_file"] else None
            file_name = button["download_file"]["filename"]

            download_function = create_download_function(f"data:{file_mime_type};base64,{file_data}", file_name)

            button["onClick"] = download_function

    component_value = _component_func(buttons=buttons, group_style=group_style, div_id=div_id, div_style=div_style, disabled=disabled, key=key, return_value=return_value,
                                      mode=mode, shape=shape, size=size, theme=theme, height=height)

    if return_value:
        return component_value
