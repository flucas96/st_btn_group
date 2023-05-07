import streamlit as st
from st_btn_group import st_btn_group

import base64
import pandas as pd
from io import BytesIO

# Create a sample dataframe
data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
df = pd.DataFrame(data)

# Save the dataframe to an Excel file in memory
buffer = BytesIO()
df.to_excel(buffer, index=False, engine='openpyxl')
buffer.seek(0)

# Encode the Excel file as base64
encoded_excel = base64.b64encode(buffer.getvalue()).decode('utf-8')


st.set_page_config(page_title="Streamlit Button Group Component", layout="wide")

st.title("Streamlit Button Group Component")


buttons = [
    {
        "label": "Button 1",
        "style": {"backgroundColor": "red", "color": "white"},
    },
    {
        "label": "Button 2",
        
    },
    {
        "label": "Button 3",
        "style": {"backgroundColor": "green", "color": "white"},
    },
]



buttons = [
    {
        "label": "Download Excel",
        "download_file": {"data": encoded_excel, "mime_type": None, "filename": "test.xlsx"},
    },
    # Add more buttons as needed
]
st_btn_group(buttons=buttons, key="3", return_value=False, align="right" )

st_btn_group(buttons=buttons, key="4", align="center")
buttons = [
    {
        "label": "Streamlit Button",
        "style": {
            "backgroundColor": "#F63366",
            "color": "#FFFFFF",
            "border": "1px solid #F63366",
            "borderRadius": "3px",
            "padding": "0.25rem 1rem",
            "fontSize": "1rem",
            "cursor": "pointer",
            "textDecoration": "none",
            "transition": "all 0.2s ease-in-out"
        },
    },
]



st_btn_group(buttons=buttons, key="5", align="center")

st_btn_group(
    buttons=[
        {
            "label": "<strong>First Button</strong>",
            "frontIcon": "Fa-Home",
            "endEnhancer": "<em>Text</em>",
        },
        {
            "label": "<strong>Second Button</strong>",
            "endIcon": "Md-Home",
            "startEnhancer": "<em>Text</em>",
        },
        {
            "label": "<strong>Third Button</strong>",
            "frontIcon": "Ant-Home",
            "endEnhancer": "<em>Text</em>",
        },
    ],key="7", align="center")
st_btn_group(buttons=buttons, key="6", align="right")


st_btn_group(
    buttons=[
        {
            "label": "<strong>First Button</strong>",
            "frontIcon": "FaHome",
            "endEnhancer": "<em>Text</em>",
        },
        {
            "label": "<strong>Second Button</strong>",
            "endIcon": "MdHome",
            "startEnhancer": "<em>Text</em>",
        },
        {
            "label": "<strong>Third Button</strong>",
            "frontIcon": "AntHome",
            "endEnhancer": "<em>Text</em>",
        },
    ],key="8", align="center")


btns = [{
    "label": "<strong>First Button</strong>",
    "frontIcon": "Fa-Home",
    "endEnhancer": "<em>Text</em>",
},
{
    "label": "<strong>Second Button</strong>",
    "endIcon": "Md-Home",
    "startEnhancer": "<em>Text</em>",
},
{
    "label": "<strong>Third Button</strong>",
    "frontIcon": "Ant-Home",
    "endEnhancer": "<em>Text</em>",
}]

st_btn_group(buttons=btns, key="9", align="center", mode="checkbox")


buttons = [
    {
        "label": "<strong>First Button</strong>",
        "frontIcon": "Fa-Home",
        "endEnhancer": "<em>Text</em>",
        "frontIconStyle": {"color": "red", "fontSize": "20px"},
    },
    {
        "label": "<strong>Second Button</strong>",
        "endIcon": "Md-Home",
        "startEnhancer": "<em>Text</em>",
        "backIconStyle": {"color": "blue", "fontSize": "20px"},
    },
    {
        "label": "<strong>Third Button</strong>",
        "frontIcon": "Ant-Home",
        "endEnhancer": "<em>Text</em>",
        "frontIconStyle": {"color": "green", "fontSize": "20px"},
    },
]

st_btn_group(buttons=buttons, key="10", align="center")

buttons = [
    {
        "label": "<strong>First Button</strong>",
        "frontIcon": "Fa-Home",
        "endEnhancer": "<em>Text</em>",
        "frontIconStyle": {"color": "red", "fontSize": "20px"},
    },
    {
        "label": "<strong>Second Button</strong>",
        "endIcon": "Md-Home",
        "startEnhancer": "<em>Text</em>",
        "backIconStyle": {"color": "blue", "fontSize": "20px"},
    },
    {
        "label": "<strong>Third Button</strong>",
        "frontIcon": "Ai-Home",
        "endEnhancer": "<em>Text</em>",
        "frontIconStyle": {"color": "green", "fontSize": "20px"},
    },
]

st_btn_group(buttons=buttons, key="11", align="center")