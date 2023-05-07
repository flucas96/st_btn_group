import streamlit as st
from st_btn_group import st_btn_group

st.set_page_config(layout="wide")

st.title("Streamlit Button Group Component")

# Sidebar configuration
st.sidebar.header("Configuration")

button_count = st.sidebar.slider("Number of buttons", 1, 5, 3)
buttons = []

for i in range(button_count):
    label = st.sidebar.text_input(f"Button {i+1} label", f"Button {i+1}")
    value = st.sidebar.text_input(f"Button {i+1} value", str(i+1))
    kind = st.sidebar.selectbox(f"Button {i+1} kind", ["primary", "secondary", "minimal", "tertiary"], key=f"kind_{i}")
    disabled = st.sidebar.checkbox(f"Disable Button {i+1}", value=False, key=f"disabled_{i}")
    buttons.append({"label": label, "value": value, "kind": kind, "disabled": disabled})

group_style = {"padding-top": "5px"}
shape = st.sidebar.selectbox("Button shape", ["default", "pill", "round", "circle", "square"])
size = st.sidebar.selectbox("Button size", ["default", "large", "compact", "mini"])
mode = st.sidebar.selectbox("Button group mode", ["defaut","checkbox", "radio"])
theme = st.sidebar.selectbox("Theme", ["light", "dark"])

# Button group component
result = st_btn_group(
    buttons=buttons,
    group_style=group_style,
    shape=shape,
    size=size,
    mode=mode,
    theme=theme
)

# Display selected button value

st.write(f"Selected button value: {result}")