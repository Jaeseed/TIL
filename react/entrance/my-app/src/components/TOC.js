import React, { Component } from 'react'

class TOC extends Component {
  // component를 update하는지 여부를 정해주는 함수
  // newProps와 newState를 기본 인자로 받는 함수이다.
  // return false일 때 render 동작을 하지 않는다.
  shouldComponentUpdate(newProps, newState) {
    if (this.props.data === newProps.data) {
      return false;
    } 
    return true;
  }
  render () {
    var lists = [];
    var data = this.props.data;
    var i = 0;
    while (i < data.length){
      lists.push(
        <li key={data[i].id}>
          {/* id를 가져오는 방식 2가지 */}
          <a 
            href={"/content/" +data[i].id}
            data-id={data[i].id}
            onClick={function(e){
              e.preventDefault()
              this.props.onChangePage(e.target.dataset.id);
            }.bind(this)}
          >{data[i].title}</a>
        </li>);
      i = i + 1;
    }
    return (
      <nav>
        <ul>
          {lists}
        </ul>
      </nav>
    );
  }
}


export default TOC;