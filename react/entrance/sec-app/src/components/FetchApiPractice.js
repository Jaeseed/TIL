import React, {Component} from "react";

class FetchApiPractice extends Component {
  constructor() {
    super();
    this.state = {forecasts: [], loading: true};

  }
  
  componentDidMount() {
    this.setState({loading:true});
    fetch("/weatherforecast")
      .then(response => response.json())
      .then(data => {this.setState({forecasts: data, loading: false});});
  }

  // static 메서드?
  static displayData(forecasts) {
    console.log(forecasts);
    return (
      <table>
        {forecasts.map(forecasts =>
          <tr>
            <td>{forecasts.date}</td>
            <td>{forecasts.temperatureC}</td>
          </tr>
        )}
      </table>
    );
  }

  render() {
    let contents = this.state.loading ? <p>loading...</p> : FetchApiPractice.displayData(this.state.forecasts);
    return (
      <>
        {contents}
      </>
    )
  }
}

export default FetchApiPractice