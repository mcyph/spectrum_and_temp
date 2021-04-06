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
    // Convert to arrays of [[column, value], ...]
    const valuesOut = [];
    for (const k in this.data) {
      if (k === 'datetime') {
        continue
      }
      valuesOut.push([k, this.data[k]]);
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
        dataZoom={[
          {
            show: true,
            type: "slider",
            moveHandleSize: 20,
            moveHandleStyle: {
              opacity: 0.3
            },
            start: 0,
            end: utilityFns.isMobile() ? 5 : 11
          }, {
            type: "inside"
          }
        ]}
        style={{
          height: utilityFns.isMobile() ? "calc(66vh)" : "calc(50vh - 33px)",
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
