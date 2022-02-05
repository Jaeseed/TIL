import React, { Component } from 'react'

class Subject extends Component {
  // 원래는 function이 붙는데 javascript에서 생략 가능
  render (){
    // 하나의 최상위 태그만 써야 함
    return (
      <header>
        <h1><a href="/" onClick={function(e){
          e.preventDefault();
          this.props.onChangePage();
        }.bind(this)}>{this.props.title}</a></h1>
        {this.props.sub}
      </header>
    );
  }
}
export default Subject