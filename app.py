import streamlit as st
from st_btn_group import st_btn_group

import base64
import pandas as pd
from io import BytesIO


st.set_page_config(page_title="Streamlit Button Group Component", layout="wide")

st.title("Streamlit Button Group Component")

st.markdown("Install using pip: `pip install st-btn-group` (https://pypi.org/project/st-btn-group/)")
st.divider()

st.subheader("As a Download Button")
# Create a sample dataframe
data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
col1,col2 = st.columns((0.2,1))
df = pd.DataFrame(data)
with col1:
    st.dataframe(df)
# Save the dataframe to an Excel file in memory
data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
buffer = BytesIO()
df.to_excel(buffer, index=False, engine='openpyxl')
buffer.seek(0)

# #Generate a realy large dataframe to stress the system
# data = {'col1': [1, 2, 3]*100000, 'col2': [4, 5, 6]*100000}
# df = pd.DataFrame(data)
# buffer = BytesIO()
# df.to_excel(buffer, index=False, engine='openpyxl')
# buffer.seek(0)

# Encode the Excel file as base64
encoded_excel = base64.b64encode(buffer.getvalue()).decode('utf-8')


buttons = [
    {   "startEnhancer": "<i class='fas fa-download'></i>",
        "label": "Download Excel",
        "download_file": {"data": encoded_excel, "filename": "test.xlsx","large_file":False},
    },
]
with col1:
    st_btn_group(buttons=buttons, key="download_button", return_value=False)

with col2:
    st.code("""
# Create a sample dataframe
data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
df = pd.DataFrame(data)
# Save the dataframe to an Excel file in memory
buffer = BytesIO()
df.to_excel(buffer, index=False, engine='openpyxl')
buffer.seek(0)
# Encode the Excel file as base64
encoded_excel = base64.b64encode(buffer.getvalue()).decode('utf-8')
buttons = [{"startEnhancer": "<i class='fas fa-download'></i>",
        "label": "Download Excel",
        "download_file": {"data": encoded_excel, "filename": "test.xlsx"},},]
st_btn_group(buttons=buttons, key="download_button", return_value=False)
""", language="python")
    

st.divider()

st.subheader("Different Shapes, Sizes and other options")

shapes, sizes,align, disabled,_ = st.columns((1,1,1,1,5))
merged, gap, divider,_ = st.columns((1,1,1,6))
shape = shapes.selectbox("Shape", ["default", "pill", "round", "circle", "square"], index=0)
size = sizes.selectbox("Size", ["default", "large", "compact", "mini"], index=0)
align = align.selectbox("Align", ["left", "center", "right"], index=0)
disabled = disabled.checkbox("Disabled", value=False)

merge_buttons = merged.checkbox("Merge Buttons", value=False)
gap_between_buttons = gap.slider("Gap between Buttons", min_value=0, max_value=100, value=5)
display_divider = divider.checkbox("Display Divider", value=False)


buttons = [
    {   "label": "Button 1",
        "value": "1",
    },
    {   "label": "Button 2",
        "value": "2",
    },
    {   "label": "Button 3",
        "value": "3",
    },
]


returned = st_btn_group(buttons=buttons, key="1", shape=shape, size=size, align=align, disabled= disabled, return_value=True, merge_buttons=merge_buttons, gap_between_buttons=str(gap_between_buttons), display_divider=display_divider)

if returned:
    st.write("button clicked")

st.write("Returned Value:", returned)


st.code("""
buttons = [
{   "label": "Button 1",
    "value": "1",
},
{   "label": "Button 2",
    "value": "2",
},
{   "label": "Button 3",
    "value": "3",
},
]
st_btn_group(buttons=buttons, key="1", shape='""" + shape + """', size='"""+ size + """', align ='"""+align+"""', disabled = """+str(disabled)+""" merge_buttons = """  +str(merge_buttons)+""", gap_between_buttons = """+str(gap_between_buttons) + """, display_divider = """+str(display_divider) + """, return_value = False)
"""
, language="python")

st.divider()

st.subheader("Different Modes")

modes,_,_ = st.columns((1,1,5)) 
mode = modes.selectbox("Mode", ["default", "checkbox", "radio"], index=0)
st.info("**Caution:** Change the mode in this demo might lead to weird outputs, because the button value is not reseted when the mode is changed")

buttons = [
    {   "label": "Button 1",
        "value": "1",
    },
    {   "label": "Button 2",
        "value": "2",
    },
    {   "label": "Button 3",
        "value": "3",
    },
    {   "label": "Button 4",
        "value": "4",},
    {   "label": "Button 5",
        "value": "5",}
]

btn,code = st.columns((1,1))
with btn:
    returned = st_btn_group(buttons=buttons, key="2", mode=mode, return_value=True)
    st.write("Returned Value:", returned)

with code:
    st.code("""
buttons = [
    {   "label": "Button 1",
        "value": "1",
    },
    {   "label": "Button 2",
        "value": "2",
    },
    {   "label": "Button 3",
        "value": "3",
    },
    {   "label": "Button 4",
        "value": "4",},
    {   "label": "Button 5",
        "value": "5",}
]
returned = st_btn_group(buttons=buttons, key="2", mode='"""+mode+""", return_value=True)
st.write("Returned Value:", returned)
""", language="python")

st.divider()

st.subheader("Theming and Styling")

themes,_ = st.columns((1,6))
theme = themes.selectbox("Theme", ["light", "dark"], index=0)

buttons = buttons = [
    {   "label": "Button 1",
        "value": "1",
    },
    {   "label": "Button 2",
        "value": "2",
    }
]
btn,code = st.columns((1,3))
with btn:
    st_btn_group(buttons=buttons, key="4", theme=theme)
with code:
    st.code("""
buttons = buttons = [
    {   "label": "Button 1",
        "value": "1",
    },
    {   "label": "Button 2",
        "value": "2",
    }
]
st_btn_group(buttons=buttons, key="4", theme='"""+theme+"""')
""", language="python")

st.markdown("#### Custom CSS Styling")
st.markdown("###### Example 1")

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
btn,code = st.columns((1,3))
with btn:
    return_val = st_btn_group(buttons=buttons, key="5")
    st.write(return_val)
with code:
    st.code("""
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

st_btn_group(buttons=buttons, key="5")
""", language="python")

st.markdown("###### Example 2")


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

btn,code = st.columns((1,3))
with btn:
    st_btn_group(buttons=buttons, key="6")
with code:
    st.code("""
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
st_btn_group(buttons=buttons, key="6")""", language="python")
   