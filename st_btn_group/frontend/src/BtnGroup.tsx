import React, { useEffect, useState } from "react";

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
import { Helmet } from 'react-helmet';


type ButtonProps = {
  label: string;
  disabled?: boolean;
  kind?: "primary" | "secondary" | "tertiary";
  size?: string;
  shape?: string;
  value?: string;
  overrides?: any;
 
  startEnhancer?: string;
  endEnhancer?: string;
  onClick?: string;
  style?: React.CSSProperties;

};


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
    <>
      <Helmet>
        <link
          rel="stylesheet"
          href="https://pro.fontawesome.com/releases/v5.10.0/css/all.css"
          integrity="sha384-AYmEC3Yw5cVb3ZcuHtOA93w35dYTsvhLPVnYs9eStHfGJvOvKxVfELGroGkvsg+p"
          crossOrigin="anonymous"
        />
      </Helmet>
      <StyletronProvider value={engine}>
        <ThemeProvider theme={theme === "dark" ? DarkTheme : LightTheme}>
          <div id={div_id} style={div_style}>
            <StatefulButtonGroup
              key={key}
              mode={
                mode === "checkbox" || mode === "radio"
                  ? MODE[mode as keyof typeof MODE]
                  : undefined
              }
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
                      {button.startEnhancer && (
                        <span dangerouslySetInnerHTML={{ __html: button.startEnhancer }} />
                      )}
                    </>
                  )}
                  endEnhancer={() => (
                    <>
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
    </>
  );
};
export default withStreamlitConnection(BtnGroup);