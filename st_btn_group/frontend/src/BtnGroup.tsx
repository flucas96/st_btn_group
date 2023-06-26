import React, { useEffect, useState, useRef } from "react";

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
    div_id,
    div_style,
    custom_fontawesome_url
  } = props.args;

  const { buttons } = props.args as { buttons: ButtonProps[] };

 const [selectedValues, setSelectedValues] = useState<string[]>([]);

 const handleClick = (
  event: React.SyntheticEvent<HTMLButtonElement, Event>,
  index: number,
  value: string
) => {
  // Use the index as the value if the value is not defined or is an empty string
  value = value || value === "" ? index.toString() : value;

  if (mode === "checkbox") {
    const idx = selectedValues.indexOf(value);
    if (idx !== -1) {
      selectedValues.splice(idx, 1);
    } else {
      selectedValues.push(value);
    }
    setSelectedValues([...selectedValues]);
  } else if (mode === "radio") {
    setSelectedValues([value]);
  } else {
    // Normal button mode
    if (selectedValues.includes(value)) {
      setSelectedValues([]);
    } else {
      setSelectedValues([value]);
    }
  }
};

useEffect(() => {
  if (return_value) {
    Streamlit.setComponentValue(selectedValues);
  }
}, [selectedValues, return_value]);


  // Create a ref for the button group wrapper
  const wrapperRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (wrapperRef.current) {
      // Measure the height of the wrapper
      const height = wrapperRef.current.offsetHeight + 1;

      // Set the iframe height to the height of the wrapper
      Streamlit.setFrameHeight(height);
    }
  }, [wrapperRef]);


  return (
    <>
  <Helmet>
  <script src={custom_fontawesome_url} crossOrigin="anonymous" id="font-awesome-icons"></script> 
  <style>{`
    .first-button {
      border-top-right-radius: 0;
      border-bottom-right-radius: 0;
      margin-right: 0;
    }
    .middle-button {
      border-radius: 0;
      margin-right: 0;
    }
    .middle-button.merge-dividers {
      border-right: 1px solid #ccc;
      border-left: 1px solid #ccc;
    }
    .last-button {
      border-top-left-radius: 0;
      border-bottom-left-radius: 0;
      margin-left: 0;
    }
  `}</style>
</Helmet>
      <StyletronProvider value={engine}>
        <ThemeProvider theme={theme === "dark" ? DarkTheme : LightTheme}>
          <div id={div_id} style={div_style} ref={wrapperRef}>
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
              
{buttons.map((button, index) => {
  let buttonClass = '';
  if (props.args.merge_buttons) {
    if (index === 0) {
      buttonClass = 'first-button';
    } else if (index === buttons.length - 1) {
      buttonClass = 'last-button';
    } else {
      buttonClass = 'middle-button';
      if (props.args.display_divider) {
        buttonClass += ' merge-dividers';
      }
    }
  }
  return (
    <Button
      key={key + "_" + index}
      className={buttonClass}
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
  );
})}
            </StatefulButtonGroup>
          </div>
        </ThemeProvider>
      </StyletronProvider>
    </>
  );
};
export default withStreamlitConnection(BtnGroup);