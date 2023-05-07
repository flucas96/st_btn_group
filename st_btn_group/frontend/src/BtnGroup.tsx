import React, { useEffect, useState } from "react";
import { ReactElement } from "react";

import {
  ComponentProps,
  Streamlit,
  withStreamlitConnection,
} from "streamlit-component-lib";
import { Button } from "baseui/button";
import {
  StatefulButtonGroup,
  MODE,
} from "baseui/button-group";
import { Client as Styletron } from "styletron-engine-atomic";
import { Provider as StyletronProvider } from "styletron-react";
import { LightTheme, DarkTheme } from "baseui";
import { ThemeProvider } from "baseui";

import { CSSProperties } from 'react';
import * as FontAwesome from 'react-icons/fa';
import * as MaterialDesign from 'react-icons/md';
import * as AntDesign from 'react-icons/ai';

type ButtonProps = {
  label: string;
  disabled?: boolean;
  kind?: "primary" | "secondary" | "tertiary";
  size?: string;
  shape?: string;
  value?: string;
  overrides?: any;
  frontIcon?: string;
  endIcon?: string;
  startEnhancer?: string;
  endEnhancer?: string;
  onClick?: string;
  style?: React.CSSProperties;
  frontIconStyle?: React.CSSProperties;
  backIconStyle?: React.CSSProperties;
};




function getIcon(icon: string | undefined, iconStyle?: CSSProperties): JSX.Element | null {
  if (!icon) {
    return null;
  }



  const [library, iconName] = icon.split("-");

  console.log("Library: ", library);
  console.log("IconName: ", iconName);

  if (library === "Fa" && iconName) {
    //iconsMap['fa'+upperFirst(camelCase(item.iconName)) as keyof typeof iconsMap]
    const IconComponent = FontAwesome[iconName as keyof typeof FontAwesome];
    console.log("IconComponent (Fa): ", IconComponent);
    return IconComponent ? React.createElement(IconComponent, { style: iconStyle }) : null;
  } else if (library === "Md" && iconName) {
    const IconComponent = MaterialDesign[iconName as keyof typeof MaterialDesign];
    console.log("IconComponent (Md): ", IconComponent);
    return IconComponent ? React.createElement(IconComponent, { style: iconStyle }) : null;
  } else if (library === "Ai" && iconName) {
    const IconComponent = AntDesign[iconName as keyof typeof AntDesign];
    console.log("IconComponent (Ai): ", IconComponent);
    return IconComponent ? React.createElement(IconComponent, { style: iconStyle }) : null;
  }

  return null;
}
const engine = new Styletron();

const BtnGroup = (props: ComponentProps) => {
  const {
    key,
    group_style,
    return_value,
    mode,
    disabled,
    theme,
    height,
    div_id,
    div_style,
  } = props.args;

  const { buttons } = props.args as { buttons: ButtonProps[] };
  const [selectedIndices, setSelectedIndices] = useState<number[]>([]);

  const handleClick = (
    event: React.SyntheticEvent<HTMLButtonElement, Event>,
    index: number,
    value: string
  ) => {
    if (mode === "checkbox") {
      const idx = selectedIndices.indexOf(index);
      if (idx !== -1) {
        selectedIndices.splice(idx, 1);
      } else {
        selectedIndices.push(index);
      }
      setSelectedIndices([...selectedIndices]);
    } else if (mode === "radio") {
      setSelectedIndices([index]);
    } else {
      // Normal button mode
      if (selectedIndices.includes(index)) {
        setSelectedIndices([]);
      } else {
        setSelectedIndices([index]);
      }
    }
  };

  useEffect(() => {
    if (return_value) {
      Streamlit.setComponentValue(Array.from(selectedIndices.values()));
    }
  }, [selectedIndices, return_value]);

  useEffect(() => {
    Streamlit.setFrameHeight(height);
  }, []);

  return (
    <StyletronProvider value={engine}>
      <ThemeProvider theme={theme === "dark" ? DarkTheme : LightTheme}>
        <div id={div_id} style={div_style}>
          <StatefulButtonGroup
            key={key}
            mode={mode === "checkbox" || mode === "radio" ? MODE[mode as keyof typeof MODE] : undefined}
            initialState={{ selected: [] }}
              shape={props.args.shape || "default"}

              size={props.args.size || "default"}
            onClick={(event, index) => {
              handleClick(event, index, buttons[index].value || "");
              if (buttons[index].onClick) {
                eval(buttons[index].onClick || "");
              }
            }}
            overrides={{
              Root: {
                style: group_style,
              },
            }}
          >
            {buttons.map((button, index) => (
              <Button
                key={key + "_" + index}
                disabled={button.disabled || disabled}
                kind={button.kind || props.args.kind}
                startEnhancer={() => (
                  <>
                    {getIcon(button.frontIcon, button.frontIconStyle)}
                    {button.startEnhancer && (
                      <span dangerouslySetInnerHTML={{ __html: button.startEnhancer }} />
                    )}
                  </>
                )}
                endEnhancer={() => (
                  <>
                    {getIcon(button.endIcon, button.backIconStyle)}
                    {button.endEnhancer && (
                      <span dangerouslySetInnerHTML={{ __html: button.endEnhancer }} />
                    )}
                  </>
                )}
                style={button.style}
              >
                <span dangerouslySetInnerHTML={{ __html: button.label }} />
              </Button>
            ))}
          </StatefulButtonGroup>
        </div>
      </ThemeProvider>
    </StyletronProvider>
  );
};

export default withStreamlitConnection(BtnGroup);