import streamlit.components.v1 as components
import os
import mimetypes
import logging
import base64
import re 
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
    """
    Download a file using the data URL pattern (small files)
    """
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

def create_download_function_large_files(file_data: str, file_name: str, file_mime_type: str = None) -> str:
    """
    Using the fetch API to download large files
    """
    # Remove whitespaces
    file_data = file_data.replace(' ', '')

    # Check if the data is Base64 encoded
    is_base64 = re.match('^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{4})$', file_data)
    if not is_base64:
        raise ValueError("The provided file data is not Base64 encoded.")

    # Create the JavaScript function with the data URL, including the data: prefix and the mime type
    return f"""(function() {{
        const link = document.createElement('a');
        link.download = '{file_name}';

        const fileData = atob('{file_data}');
        const byteCharacters = fileData;
        const byteArrays = [];
        for (let offset = 0; offset < byteCharacters.length; offset += 512) {{
            const slice = byteCharacters.slice(offset, offset + 512);
            const byteNumbers = new Array(slice.length);
            for (let i = 0; i < slice.length; i++) {{
                byteNumbers[i] = slice.charCodeAt(i);
            }}
            const byteArray = new Uint8Array(byteNumbers);
            byteArrays.push(byteArray);
        }}

        const blob = new Blob(byteArrays, {{ type: '{file_mime_type}' }});
        const url = URL.createObjectURL(blob);

        fetch(url)
            .then(response => {{
                if (response.ok) {{
                    return response.blob();
                }} else {{
                    throw new Error('Failed to fetch the file.');
                }}
            }})
            .then(blob => {{
                const downloadUrl = URL.createObjectURL(blob);
                link.href = downloadUrl;
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
                URL.revokeObjectURL(downloadUrl);
            }})
            .catch(error => {{
                console.error('Error creating download link:', error);
            }})
            .finally(() => {{
                URL.revokeObjectURL(url);
            }});
    }})()"""


def st_btn_group(buttons: list, group_style:dict={}, key:str = "first_carousel", return_value = True, shape:str="default",disabled:bool=False, size:str="default",
                 mode:str="default",theme:str="light", height:int=None, align:str="left", custom_fontawesome_url:str="https://kit.fontawesome.com/c7cbba6207.js", merge_buttons=False,
                 gap_between_buttons:int=5,display_divider=False, additionalHeight:int=0):
    
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

    height: int, optional - height of the button group  - deprecated
    additionalHeight: int, optional - additional height of the button group - I noticed that sometimes the height of the component is not calculated correctly. This parameter can be used to add additional height to the component
    align: str, optional - left, center, right

    custom_fontawesome_url: str, optional - if you want to use fontawesome icons you can provide a custom url to the fontawesome script

    merge_buttons: bool, optional - if True the buttons will be visible merged into one button group. If False each button will be in its own button group
    """

    if merge_buttons:
        if len(buttons) == 1:
            merge_buttons = False
            logging.warning("merge_buttons is True but only one button is provided. merge_buttons will be set to False")

    default_group_style = {
        "marginTop": "4px",
        "marginLeft": "4px",
        "gap": f"{gap_between_buttons}px !important",
    }

    for css_op in default_group_style:
        if css_op not in group_style:
            group_style[css_op] = default_group_style[css_op]
    
    group_style["gap"] = f"{gap_between_buttons}px !important"

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
            # Get the data, filename, and optional mime type from the button dictionary
            file_data = button["download_file"]["data"]
            file_name = button["download_file"]["filename"]
            file_mime_type = button["download_file"]["mime_type"] if "mime_type" in button["download_file"] else None

            # Guess the mime type from the file name if it's not provided
            if not file_mime_type:
                file_mime_type, _ = mimetypes.guess_type(file_name)

            # Create the download function with the data in the correct format
            # Pass only the Base64 data to the function, not the full data URL
            if "large_file" in button["download_file"]:
                if button["download_file"]["large_file"] == True:
                    download_function = create_download_function_large_files(file_data, file_name, file_mime_type)
                else:
                    download_function = create_download_function(f"data:{file_mime_type};base64,{file_data}", file_name)
            else:
                    download_function = create_download_function(f"data:{file_mime_type};base64,{file_data}", file_name)


            button["onClick"] = download_function

    component_value = _component_func(buttons=buttons, group_style=group_style, div_id=div_id, div_style=div_style, disabled=disabled, key=key, return_value=return_value,
                                      mode=mode, shape=shape, size=size, theme=theme, custom_fontawesome_url = custom_fontawesome_url,merge_buttons=merge_buttons,
                                      display_divider=display_divider, additionalHeight=additionalHeight)

    if return_value:

        if mode in ["default","radio"]:
            if isinstance(component_value, list):
                if len(component_value) == 1:
                    return component_value[0]
                
        return component_value
