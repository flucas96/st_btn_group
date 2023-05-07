import streamlit.components.v1 as components
import os

import logging


_RELEASE = False


if not _RELEASE:
    _component_func = components.declare_component(
        # We give the component a simple, descriptive name ("my_component"
        # does not fit this bill, so please choose something better for your
        # own component :)
        "st_btn_group",
        # Pass `url` here to tell Streamlit that the component will be served
        # by the local dev server that you run via `npm run start`.
        # (This is useful while your component is in development.)
        url="http://localhost:3000",
    )
else:
    # When we're distributing a production version of the component, we'll
    # replace the `url` param with `path`, and point it to to the component's
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("st_btn_group", path=build_dir)

def st_btn_group(buttons: list, group_style:dict={"padding-top":"5px"},key:str = "first_carousel", return_value = True, shape:str="default",disabled:bool=False, size:str="default",
                 mode:str="defaukt",theme:str="light", height:int="50px"):
    """

    Parameters
    ----------
    key : str, optional 

    buttons: list of dict. example [{"label": "<h1> Button 1</h1>","disabled":False,"kind":"primary","size":"default","shape":"default", "value":"1", "onClick":"console.log('clicked')", "startEnhancer":"<h1>Start</h1>", "endEnhancer":"<h1>Ende</h1>", style={"backgroundColor":"red"}}]
    group_style: dict, optional

    return_value: bool, optional - If False Streamlit wont receive any value from the component
    disabled: bool, optional - Disables the whole Button group

    shape: str, optional - default, pill, round, circle, square
    size: str, optional - default, large, compact, mini
    mode: str, optional - default, checkbox, radio

    theme: str, optional - light, dark

    """
   
       
    component_value = _component_func(buttons=buttons, group_style=group_style, disabled=disabled,key=key, return_value=return_value,
                                      mode = mode, shape=shape, size=size, theme=theme)

    if return_value:
        return component_value
