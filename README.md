# Streamlit Button Group Component

This is a custom Streamlit button group component that allows you to create groups of buttons with various options and styles.

## Installation

1. Install the required dependencies with `pip install st-btn-group`.

## Usage

First, import the `st_btn_group` function from the `st_btn_group` package:

```python
from st_btn_group import st_btn_group

```

Then, use the `st_btn_group` function to create a button group:

```python
st_btn_group(
    buttons=[{"label": "Button 1", "value": "1"}, {"label": "Button 2", "value": "2"}],   
)    
```

## Parameters

The `st_btn_group` function accepts the following parameters:

- `mode`: The mode of the buttons. The input must be a string. Possible values are `default`, `checkbox`, `radio`.
   
    - If `default`, the buttons will behave like normal buttons. 

    - If `checkbox`, the buttons will behave like checkboxes. The `value` of the button will be returned as a list of values when the button is clicked.
    
    - If `radio`, the buttons will behave like radio buttons. The `value` of the button will be returned as a single value when the button is clicked. The button will keep a selected state when clicked. To unselect the button, click on it again.


- `buttons`: A list of dictionaries containing the buttons to be displayed in the group. Each dictionary must contain a `label` and a `value` key. The `label` key is used to display the button's label, while the `value` key is used to identify the button when it is clicked. The `value` key can be anything.

    - Possible parameters (keys of the dictionary) for each button are:

        - `label`: The label of the button. This is the only required parameter. HTMLS tags are allowed. FontAwesome Icons will be display if integrated over html tags. For example, `<i class="fas fa-home"></i> Home`.

        - `value`: The value of the button. This is the value that will be returned when the button is clicked. If not specified, the `label` value will be used.

        - `style`: The style of the button. The input must be a dictionary like this one `{"color": "red", "font-size": "20px"}`

        - `disabled`: Whether the button is disabled or not. The input must be a boolean.

        - `onClick`: A JavaScript Function as string that will be executed when the button is clicked. For example, `onClick="alert("clicked")"`.

        - `startEnhancer`: A string that will be displayed before the button's label. For example, `startEnhancer="<i class="fas fa-home"></i>"`.

        - `endEnhancer`: A string that will be displayed after the button's label. For example, `endEnhancer="<i class="fas fa-home"></i>"`.

        - `download_file`: Functionality to download a file directly when the button gets clicked without a callback to Streamlit. The input must be a dictionary like this one `{"filename": "file.xlsx", "data": base64 data, "mime_type": "mime Typ" (optional)}`. The mime_type is optional and will be guess using the file extension of the filename. The data must be base64 encoded. You can use the `base64` library to encode your data. For example, `base64.b64encode(data.encode()).decode()`.

- Example: 
```python
st_btn_group(
    buttons=[
        {
            "label": "Button 1",
            "value": "1",
            "style": {"color": "red", "font-size": "20px"},
            "disabled": True,
            "onClick": "alert('clicked')",
            "startEnhancer": "<i class='fas fa-home'></i>",
            "endEnhancer": "<i class='fas fa-home'></i>",
            "download_file": {
                "filename": "file.xlsx",
                "data": base64.b64encode(data.encode()).decode(),
                "mime_type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            },
        },
        {"label": "Button 2", "value": "2"},
    ],
)
```

- `return_value`: Whether the value of the button should be returned when the button is clicked. The input must be a boolean. If `False`, the button will not return any value when clicked. And Streamlit will not trigger a rerun when the button is clicked! 

- `shape`: The shape of the buttons. The input must be a string. Possible values are `default`, `round`, `pill`, `circle`.

- `size`: The size of the buttons. The input must be a string. Possible values are `default`, `large,` `compact`, `mini`

- `group_style`: The style of the button group. The input must be a dictionary like this one `{"display": "flex", "justify-content": "center"}`.

- `disabled`: Whether the button group is disabled or not. The input must be a boolean.


- `theme`: The theme of the buttons. The input must be a string. Possible values are `light` and `dark`.

- `align`: The alignment of the button group in streamlit. Possible values are `left`, `center`, `right`.

- `height`: The height of the button group in streamlit. Must be adjusted if the buttons are cutoff.

- `key`: An optional string to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. Multiple widgets of the same type may not share the same key.

- `custom_fontawesome_url`: Possibilty to provide a different FontAwesome URL to maybe display PRO Icons if you have a license. 



