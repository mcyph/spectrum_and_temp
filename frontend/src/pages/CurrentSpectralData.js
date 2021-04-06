import React from "react";

import BasicBarChart from "./BasicBarChart";
import utilityFns from "./utilityFns";

class CurrentSpectralData extends React.Component {
  state = {}

  /**
   *
   */
  constructor({ data }) {
    super({ data });
  }

  render() {
    if (!this.props.data) {
      return '';
    }

    // Convert to arrays of [[column, value], ...]
    const valuesOut = [];
    for (const k in this.props.data) {
      if (k === 'datetime') {
        continue
      }
      valuesOut.push([k, [this.props.data[k], k.split('_')[2]]]);
    }

    return <>
      <BasicBarChart
        xAxisType={ BasicBarChart.AXIS_TYPE.CATEGORY }
        xAxisLabelRotate={ 60 }
        xAxisMargin={ 11 }
        yAxisType={ BasicBarChart.AXIS_TYPE.VALUE }
        gridStyle={{
          top: "40px",
          bottom: "200px",
          left: "90px",
          right: "30px"
        }}
        style={{
          height: utilityFns.isMobile() ? "calc(80vh)" : "calc(70vh - 33px)",
          marginTop: "25px",
          marginLeft: "auto",
          marginRight: "auto",
          maxWidth: "1000px"
        }}
        data={ [[this.props.name, valuesOut, this.props.color]] }
      />
    </>;
  }
}

export default CurrentSpectralData;
