// 1. component 강의

// import React, { Component } from 'react'
// import './App.css';


// class TOC extends Component {
//   render () {
//     return (
//       <nav>
//         <ul>
//           <li><a href="1.html">HTML</a></li>
//           <li><a href="2.html">CSS</a></li>
//           <li><a href="3.html">JavaScript</a></li>
//         </ul>
//       </nav>
//     );
//   }
// }

// class Content extends Component {
//   render () {
//     return (
//       <article>
//         <h2>{this.props.title}</h2>
//         {this.props.desc}
//       </article>
//     );
//   }
// }

// class Subject extends Component {
//   // 원래는 function이 붙는데 javascript에서 생략 가능
//   render (){
//     // 하나의 최상위 태그만 써야 함
//     return (
//       <header>
//         <h1>{this.props.title}</h1>
//         {this.props.sub}
//       </header>
//     );
//   }
// }


// // App이란 클래스 제작하고 react의 Component 클래스를 상속받는다.
// // App이란 클래스는 render라는 메소드가 있다 라고 이해하면 편함
// class App extends Component { 
//   render() {
//     return (
//       <div className="App">
//         <Subject title="WEB" sub="world wide web!"></Subject>
//         <Subject title="React" sub="For UI"></Subject>
//         <TOC></TOC>
//         <Content title="dd" desc="dd"></Content>
//       </div>
//     );
//   }
// }

// export default App;



// 2. components 파일로 저장

// import React, { Component } from 'react'
// import TOC from "./components/TOC"
// import Content from "./components/Content"
// import Subject from './components/Subject';
// import './App.css';


// // App이란 클래스 제작하고 react의 Component 클래스를 상속받는다.
// // App이란 클래스는 render라는 메소드가 있다 라고 이해하면 편함
// class App extends Component { 
//   render() {
//     return (
//       <div className="App">
//         <Subject title="WEB" sub="world wide web!"></Subject>
//         <Subject title="React" sub="For UI"></Subject>
//         <TOC></TOC>
//         <Content title="dd" desc="dd"></Content>
//       </div>
//     );
//   }
// }

// export default App;


import React, { Component } from 'react'
import TOC from "./components/TOC"
import Content from "./components/Content"
import Subject from './components/Subject';
import './App.css';


// App이란 클래스 제작하고 react의 Component 클래스를 상속받는다.
// App이란 클래스는 render라는 메소드가 있다 라고 이해하면 편함
class App extends Component { 
  // component 실행될 때 constructor가 초기화를 담당한다.
  constructor(props) {
    super(props);
    this.state = {
      mode: 'read',
      subject: {title: 'WEB', sub:'World Wide Web!'},
      welcome: {title: 'Welcome', desc: 'Hello, React!!'},
      contents: [
        {id:1, title: 'HTML', desc:'HTML is for information'},
        {id:2, title: 'CSS', desc:'CSS is for design'},
        {id:3, title: 'JavaScript', desc:'JavaScript is for interactive'},
      ]
    }
  }
  render() {
    var _title, _desc = null;
    if (this.state.mode === 'welcome') {
      _title = this.state.welcome.title;
      _desc = this.state.welcome.desc;
    } else if(this.state.mode === 'read') {
      _title = this.state.contents[0].title;
      _desc = this.state.contents[0].desc;
    }
    return (
      <div className="App">
        {/*<Subject 
          title={this.state.subject.title}
          sub={this.state.subject.sub}
        ></Subject>*/}
        <header>
          <h1><a href="/" onClick={function (e) {
            // 이벤트 발생 시 페이지 넘어 가는 것을 막음
            e.preventDefault();
            // 실행 시 debugger 전 단계에서 멈춤
            // debugger;
            // 이벤트 함수 내의 this는 아무 값도 가르키지 않기 때문에 함수가 끝난 직후에 bind를 추가해줘야 함
            // this.state.mode = 'welcome';
            this.setState({
              mode: 'welcome'
            })
          }.bind(this)}>{this.state.subject.title}</a></h1>
          {this.state.subject.sub}
        </header>
        <Subject title="React" sub="For UI"></Subject>
        <TOC data={this.state.contents}></TOC>
        <Content title={_title} desc={_desc}></Content>
      </div>
    );
  }
}

export default App;