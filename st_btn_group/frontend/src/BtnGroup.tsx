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
  StatefulContainerProps,
} from "baseui/button-group";
import { Client as Styletron } from "styletron-engine-atomic";
import { Provider as StyletronProvider } from "styletron-react";
import { LightTheme, DarkTheme, BaseProvider } from "baseui";

const engine = new Styletron();

const BtnGroup = (props: ComponentProps) => {
  const {
    key,
    buttons,
    group_style,
    return_value,
    shape,
    size,
    mode,
    disabled,
    theme,
  } = props.args;

  const [selectedIndices, setSelectedIndices] = useState<Set<number>>(new Set());

  const handleClick = (
    event: React.SyntheticEvent<HTMLButtonElement, Event>,
    index: number
  ) => {
    if (mode === "checkbox") {
      if (selectedIndices.has(index)) {
        selectedIndices.delete(index);
      } else {
        selectedIndices.add(index);
      }
      setSelectedIndices(new Set(selectedIndices));
    } else if (mode === "radio") {
      setSelectedIndices(new Set([index]));
    } else {
      // Normal button mode
      if (selectedIndices.has(index)) {
        setSelectedIndices(new Set());
      } else {
        setSelectedIndices(new Set([index]));
      }
    }
  };

  useEffect(() => {
    if (return_value) {
      Streamlit.setComponentValue(Array.from(selectedIndices));
    }
  }, [selectedIndices, return_value]);

  useEffect(() => {
    Streamlit.setFrameHeight();
  }, []);

  return (
    <StyletronProvider value={engine}>
      <BaseProvider theme={theme === "dark" ? DarkTheme : LightTheme}>
        <StatefulButtonGroup
          key={key}
          mode={mode === "checkbox" || mode === "radio" ? MODE[mode as keyof typeof MODE] : undefined}
          initialState={{ selected: new Set<number>() }}
          onClick={(event, index) => handleClick(event, index)}
          {...group_style}
        >
          {buttons.map((button, index) => (
            <Button
              key={index}
              disabled={button.disabled || disabled}
              kind={button.kind}
              size={button.size || size}
              shape={button.shape || shape}
              overrides={button.overrides}
              startEnhancer={button.startEnhancer}
              endEnhancer={button.endEnhancer}
            >
              {button.label}
            </Button>
          ))}
        </StatefulButtonGroup>
      </BaseProvider>
    </StyletronProvider>
  );
};

export default withStreamlitConnection(BtnGroup);

