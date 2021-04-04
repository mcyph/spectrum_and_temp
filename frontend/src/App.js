import React, { useState } from "react";

import CssBaseline from '@material-ui/core/CssBaseline';
import { createMuiTheme, ThemeProvider } from '@material-ui/core/styles';
import { AppBar, Checkbox, FormControlLabel, Tab, Tabs } from "@material-ui/core";

import FlagIcon from '@material-ui/icons/Flag';
import PublicIcon from '@material-ui/icons/Public';
import PhotoSizeSelectSmallIcon from '@material-ui/icons/PhotoSizeSelectSmall';

import './App.css';
import { World, StatesProvinces, Countries } from "./pages";

function App() {
  // Use a dark theme
  const theme = React.useMemo(
    () => createMuiTheme({ palette: { type: "dark" } })
  );

  // Get the current page element based on the selected tab
  let [currentTab, setTab] = useState("World");
  let [per100k, setPer100k] = useState(false);

  return <>
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <div style={{
        background: "#100b2a",
        minHeight: "100vh",
        paddingBottom: "50px"
      }}>
        <h1 style={{
          color: "#ccc",
          textAlign: "center",
          paddingTop: "20px",
          paddingBottom: "20px",
          margin: 0
        }}>
          Dave Morrissey's COVID-19 Dashboard Demo
        </h1>

        <AppBar position="static">
          <Tabs value={ currentTab }
                onChange={ (i, value, tab) => {setTab(value)} }
                aria-label="select the geographic scale"
                centered>
            <Tab value="World"
                 label={ <><PublicIcon />World</> } />
            <Tab value="Countries"
                 label={ <><FlagIcon />Countries</> } />
            {/*<Tab value="Counties/States/Provinces"
                 label={ <><PhotoSizeSelectSmallIcon />Counties/States/Provinces</> } />*/}
          </Tabs>
        </AppBar>

        {
          // Show only the currently selected tab
          {
            "World": <>
                <World name="Confirmed"
                       apiKey="confirmed"
                       per100k={ per100k } />
                <World name="Recovered"
                       apiKey="recovered"
                       color="#5C5" />
                <World name="Deaths"
                       apiKey="deaths"
                       color="orange" />
            </>,
            "Countries": <>
                <div style={{
                  textAlign: "center",
                  marginTop: "10px"
                }}>
                  <FormControlLabel
                    label="Show Per 100,000 People"
                    control={ <Checkbox checked={ per100k }
                                        onChange={(event)=>{
                                          setPer100k(event.target.checked);
                                        }}
                                        color="secondary" /> } />
                </div>
                <Countries name="Confirmed"
                           apiKey="confirmed"
                           per100k={ per100k } />
                <Countries name="Recovered"
                           apiKey="recovered"
                           per100k={ per100k }
                           color="#5C5" />
                <Countries name="Deaths"
                           apiKey="deaths"
                           per100k={ per100k }
                           color="orange" />
            </>,
            "Counties/States/Provinces": <>
                <StatesProvinces />
            </>,
          }[currentTab]
        }
      </div>
    </ThemeProvider>
  </>;
}

export default App;
