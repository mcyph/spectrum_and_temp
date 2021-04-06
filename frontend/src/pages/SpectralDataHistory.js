import React from "react";

import BasicBarChart from "./BasicBarChart";
import utilityFns from "./utilityFns";

class SpectralDataHistory extends React.Component {
  state = {}

  /**
   */
  constructor({ data }) {
    super({ data });
  }

  render() {
    // Convert to arrays of [[column, value], ...]
    const valuesOut = {};
    for (const data of this.props.data) {
      for (const k in data) {
        if (k === 'datetime') {
          continue
        }
        if (!valuesOut[k]) {
          valuesOut[k] = [];
        }
        valuesOut[k].push([data['datetime'], data[k]]);
      }
    }
    const out = [];
    for (const k in valuesOut) {
      out.push([k, valuesOut[k], k.split('_')[2]])
    }

    return <>
      <BasicBarChart
        xAxisType={ BasicBarChart.AXIS_TYPE.CATEGORY }
        xAxisMargin={ 20 }
        xAxisLabelRotate={ utilityFns.isMobile() ? 60 : 0 }
        yAxisType={ BasicBarChart.AXIS_TYPE.VALUE }
        gridStyle={{
          top: "40px",
          bottom: utilityFns.isMobile() ? "180px" : "40px",
          left: "90px",
          right: "30px"
        }}
        style={{
          height: utilityFns.isMobile() ? "calc(66vh)" : "calc(38vh - 33px)",
          marginTop: "25px",
          marginLeft: "auto",
          marginRight: "auto",
          maxWidth: "1000px"
        }}
        data={ out }
      />
    </>;
  }
}

export default SpectralDataHistory;
