import React from "react";

import BasicBarChart from "./BasicBarChart";
import utilityFns from "./utilityFns";

class SingleValueHistory extends React.Component {
  state = {}

  constructor({ keyName, data }) {
    super({ keyName, data });
  }

  render() {
    // Convert to arrays of [[column, value], ...]
    const valuesOut = {};
    for (const data of this.props.data) {
      for (const k in data) {
        if (k !== this.props.keyName) {
          continue
        }
        if (!valuesOut[k]) {
          valuesOut[k] = [];
        }
        valuesOut[k].push([new Date(data['datetime']), data[k], 'blue']);
      }
    }
    const out = [];
    for (const k in valuesOut) {
      out.push([k, valuesOut[k]])
    }

    return <>
      <BasicBarChart
        xAxisType={ BasicBarChart.AXIS_TYPE.TIME }
        xAxisMargin={ 20 }
        xAxisLabelRotate={ utilityFns.isMobile() ? 60 : 0 }
        yAxisType={ BasicBarChart.AXIS_TYPE.VALUE }
        gridStyle={{
          top: "60px",
          bottom: "40px",
          left: "30px",
          right: "30px"
        }}
        style={{
          height: utilityFns.isMobile() ? "calc(85vh)" : "calc(80vh - 33px)",
          marginTop: "25px",
          marginLeft: "auto",
          marginRight: "auto",
          width: "31vw",
          maxWidth: "1000px",
          float: "left",
        }}
        data={ out }
      />
    </>;
  }
}

export default SingleValueHistory;
