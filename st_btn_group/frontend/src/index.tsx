
import React from "react"
import ReactDOM from "react-dom"
import BtnGroup from "./BtnGroup"

// Lots of import to define a Styletron engine and load the light theme of baseui


// Wrap your CustomSlider with the baseui them
ReactDOM.render(
  <React.StrictMode>
    <BtnGroup />
  </React.StrictMode>,
  document.getElementById("root")
)