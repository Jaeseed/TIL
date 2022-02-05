import React, { Component, useState, useEffect } from 'react';
import './App.css';

function App() {
  var [funcShow, setFuncShow] = useState(true);
  var [classShow, setClasscShow] = useState(true);
  return (
    <div className="container">
      <h1>Hello world!</h1>
      <input type="button" value="remove func" onClick={function(){
        setFuncShow(false);
      }}/>
      <input type="button" value="remove class" onClick={function(){
        setClasscShow(false);
      }}/>
      {funcShow? <FuncComp initNumber={1}/> : null}
      {classShow? <ClassComp initNumber={2}/> : null}
    </div>
  );
}


var funcStyle = 'color:blue';
var funcId = 1;
// 함수는 props를 함수의 인자로 받는다.
function FuncComp(props) {
  var numberState = useState(props.initNumber);
  var number = numberState[0];
  var setNumber = numberState[1];

  // 1번 방법
  // var dateState = useState(new Date().toString());
  // var _date = dateState[0];
  // var setDate = dateState[1];

  // 2번 방법
  var [_date, setDate] = useState(new Date().toString())

  useEffect(function () {
    console.log('%cfunc => useEffect (componentDidMount)' +(++funcId) , funcStyle);
    // document.title = _date
    return function () {
      console.log('%cfunc => useEffect return (componentWillUnMount))' +(++funcId) , funcStyle)
    }
  // 빈 배열을 넣으면 최초로 생성될 때 1회만 실행 됨
  }, []);
  // side effect
  useEffect(function () {
    console.log('%cfunc => useEffect (componentDidMount & componentDidUpdate)' +(++funcId) , funcStyle);
    // document.title = _date
    return function () {
      console.log('%cfunc => useEffect return (componentDidMount & componentDidUpdate)' +(++funcId) , funcStyle)
    }
  // number 값이 바뀔 때만 콜백 함수가 실행 됨
  }, [number]);
  console.log('%cfunc => render' + funcId, funcStyle);
  return (
    <div className='container'>
      <h2>function style component</h2>
      <p>Number: {number}</p>
      <p>Date: {_date}</p>
      <input type="button" value="random" onClick={
          function () {
            setNumber(Math.random());
          }
        }></input>
      <input type="button" value="random" onClick={
          function () {
            setDate(new Date().toString());
          }
        }></input>
    </div>
  );
}

var classStyle = 'color:red';
class ClassComp extends Component{
  state= {
    number:this.props.initNumber,
    date: new Date().toString()
  }
  componentWillMount(){
    console.log('%cclass => componentWillMount', classStyle)
  }
  componentDidMount(){
    console.log('%cclass => componentDidMount', classStyle)
  }
  componentWillUnmount(){
    console.log('%cclass => componentWillUnmount', classStyle)
  }
  render() {
    console.log('%cclass => render', classStyle)
    return (
      <div className='container'>
        <h2>class style component</h2>
        <p>Number: {this.props.initNumber}</p>
        <p>Number: {this.state.number}</p>
        <input type="button" value="random" onClick={
          function () {
            this.setState({number: Math.random()})
          }.bind(this)
        }></input>
        <p>Date: {this.state.date}</p>
        <input type="button" value="random" onClick={
          function () {
            this.setState({date: new Date().toString()})
          }.bind(this)
        }></input>
      </div>
    );
  }
}
export default App;
