import React, {Component} from "react";

class TextBoxonChangeEventHandler extends Component {
  constructor() {
    super();
    this.state = {
      userName: ""
    };
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(e) {
    this.setState({userName: e.target.value});
  }
  render() {
    return (
      <>
      <input type="text" placeholder="아이디" onChange={this.handleChange}/>
      <hr/>
      아이디 : {this.state.userName}
      </>
    );
  }
}

export default TextBoxonChangeEventHandler