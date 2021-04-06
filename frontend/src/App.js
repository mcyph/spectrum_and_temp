import React, { useState } from "react";

import CssBaseline from '@material-ui/core/CssBaseline';
import { createMuiTheme, ThemeProvider } from '@material-ui/core/styles';
import { AppBar, Tab, Tabs } from "@material-ui/core";

import './App.css';
import SpectralDataHistory from "./pages/SpectralDataHistory";
import CurrentSpectralData from "./pages/CurrentSpectralData";

let socket = new WebSocket("ws://localhost:8000/last_values_ws");

function App() {
  // Use a dark theme
  const theme = React.useMemo(
    () => createMuiTheme({ palette: { type: "dark" } })
  );

  // Get the current page element based on the selected tab
  let [currentTab, setTab] = useState("Spectral Data");
  let [allData, setAllData] = useState(null);

  socket.onmessage = function(event) {
    const data = JSON.parse(event.data);
    if (!allData) {
      setAllData(data);
    } else {
      const newData = JSON.parse(JSON.stringify(allData));
      for (const key in data) {
        newData[key] = data[key]
      }
      setAllData(newData);
    }
  }
  socket.onclose = function() {
    socket.close()
  }
  socket.onerror = function() {
    setAllData(null);
    socket = new WebSocket("ws://localhost:8000/last_values_ws");
  }

  const spectralCalibrated = allData ? allData['spectral_calibrated'] : [];
  const lastSpectralCalibrated = spectralCalibrated[spectralCalibrated.length-1] || null;

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
          Sensor Log Reader
        </h1>

        <AppBar position="static">
          <Tabs value={ currentTab }
                onChange={ (i, value, tab) => {setTab(value)} }
                centered>
            <Tab value="Spectral Data"
                 label={ <>Spectral Data</> } />
            <Tab value="Environment"
                 label={ <>Environment</> } />
          </Tabs>
        </AppBar>

        {
          // Show only the currently selected tab
          {
            "Spectral Data": <>
              <CurrentSpectralData data={ lastSpectralCalibrated } />
              <SpectralDataHistory data={ spectralCalibrated } />
            </>,
            "Environment": <>
            </>,
          }[currentTab]
        }
      </div>
    </ThemeProvider>
  </>;
}

export default App;
