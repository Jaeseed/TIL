## React 입문

#### 장점

- 컴포넌트
  - 가독성 - 커스텀 태그를 이용해 컴포넌트 지정 가능
  - 재사용성
  - 유지보수





#### 1. React-app 설치

- 공식 문서 방법: 프로그램을 임시로 설치, 설치할 때마다 새로 명령하여야 하고 버전 따라가기에 용이하다.
  1) npx create-react-app '앱이름' -> 앱 생성
  2) cd my-app -> 폴더 이동
  3) npm start -> 서버 실행
- npm 설치: 프로그램 영구 설치 같은 느낌
  1. npm install -g create-react-app: react 설치
  2. create-react-app -V : 버전 확인
  3. 폴더 생성 및 해당 폴더로 경로 이동
  4. create-react-app .: 디렉토리 내에 react 개발환경 구축



#### 2. 폴더 구조

- index.js가 메인
- App.js가 컴포넌트인듯



#### 3. Deploy

- npm run build: 실제 서버 환경 폴더를 만듬
- npx serve -s build ???



#### 4. Component

- 먼저 class에 대한 해석

  - App이란 클래스 제작하고 react의 Component 클래스를 상속받는다.
  - App이란 클래스는 render라는 메소드가 있다 라고 이해하면 편함

- 예시

  - ```react
    // App.js
    class Subject extends Component {
      // 원래는 function이 붙는데 javascript에서 생략 가능
      render (){
        // 하나의 최상위 태그만 써야 함
        return (
          <header>
            <h1>WEB</h1>
            world wide web!
          </header>
        );
      }
    }
    
    
    // App이란 클래스 제작하고 react의 Component 클래스를 상속받는다.
    // App이란 클래스는 render라는 메소드가 있다 라고 이해하면 편함
    class App extends Component { 
      render() {
        return (
          <div className="App">
            <Subject></Subject>
          </div>
        );
      }
    }
    ```

  - JSX란 무엇인가?

- props 기초

  - ```react
    // Subject class에서 아래와 같이 태그 안의 내용을 정의하면 컴포넌트 사용 시에 변수처럼 사용 가능
    class Subject extends Component {
      // 원래는 function이 붙는데 javascript에서 생략 가능
      render (){
        // 하나의 최상위 태그만 써야 함
        return (
          <header>
            <h1>{this.props.title}</h1>
            {this.props.sub}
          </header>
        );
      }
    }
    
    class App extends Component { 
      render() {
        return (
          <div className="App">
            <!-- Subject 클래스의 변수에 값을 지정한다. JSX 문법! -->
            <Subject title="WEB" sub="world wide web!"></Subject>
            <Subject title="React" sub="For UI"></Subject>
          </div>
        );
      }
    }
    ```

- component 파일로 분리하는 방법

  - ```react
    // React와 Component를 import함
    import React, { Component } from 'react'
    
    // 컴포넌트로 쓸 class를 작성
    class TOC extends Component {
      render () {
        return (
          <nav>
            <ul>
              <li><a href="1.html">HTML</a></li>
              <li><a href="2.html">CSS</a></li>
              <li><a href="3.html">JavaScript</a></li>
            </ul>
          </nav>
        );
      }
    }
    
    // 다른 파일에서 TOC라는 class를 쓸 수 있게 export 선언해준다.
    export default TOC;
    ```





#### 5. State

- props와 state의 차이

  - props는 component를 제어하는 방식
  - state는 component 안의 부품

- state와 props와 key의 관계를 코드로 설명한다.

  - ```react
    // 부모 component
    // class 선언 후 render 위에서 constructor로 component의 데이터를 초기화해준다.
    class App extends Component { 
      // component 실행될 때 constructor가 초기화를 담당한다.
      constructor(props) {
        super(props);
        this.state = {
          subject:{title: 'WEB', sub:'World Wide Web!'},
          contents: [
            {id:1, title: 'HTML', desc:'HTML is for information'},
            {id:2, title: 'CSS', desc:'CSS is for design'},
            {id:3, title: 'JavaScript', desc:'JavaScript is for interactive'},
          ]
        }
      }
      render() {
        return (
          <div className="App">
            <!-- 여기서 쓰는 title, sub, data는 vue에서의 v-bind와 같은 용도로 쓰인다. props를 주는 변수명이다.-->
            <Subject 
              title={this.state.subject.title}
              sub={this.state.subject.sub}
            ></Subject>
            <TOC data={this.state.contents}></TOC>
          </div>
        );
      }
    }
    
    // 자식 컴포넌트
    class TOC extends Component {
      render () {
        // 왜 let, const말고 var을 쓰는지는 모르겠다.
        var lists = [];
        // props로부터 받은 data를 TOC 클래스 내의 data라는 변수로 새로 선언한다.
        var data = this.props.data;
        var i = 0;
        while (i < data.length){
          // javascript의 push 메서드를 사용했다. li 뒤에 key는 vue에서 for문 돌렸을 때 key값을 준 것과 같다.
          // href 뒤의 내용은 나도 좀 신기하다. 문자열과 숫자가 더해지나보다 vue에서의 백틱과 비슷한 역할인 듯.
          lists.push(<li key={data[i].id}><a href={"/content/" +data[i].id}>{data[i].title}</a></li>)
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
    ```

- React에서는 state의 값이나 props의 값이 바뀌면 해당 class의 render 함수가 다시 호출 된다
  - 즉 데이터의 변화에 따라 화면이 변화한다.





#### 6. Event

- 예시

  - 아래에서 this bind에 대한 부연 설명

    - this바인딩은 함수 호출 방식에 따라 다르게 결정된다. 
    - 이벤트 핸들러 어트리뷰트의 값으로 지정한 함수는 이벤트핸들러에 의해 일반함수로 호출되고 this는 전역객체인 window를 가리키게 된다. 
    - 다만 'strict mode'가 적용된 일반 함수 내부의 this에는 window객체가 아닌 undefined가 바인딩 되는데,  class의 내부는 암묵적으로 strict mode가 적용되기 때문에 this는 undefined가 된다.
    - 그러나 bind메서드를 사용해서 명시적으로 this를 바인딩 해줌으로써 this가 App Class를 가리키도록 한다.

  - ```react
    // 1. 이벤트를 태그 안에서 발생 시키고 함수도 안에서 호출함
    // 2. e라는 인자를 선언하는 것이 어떤 방식인 지는 잘 모름
    // 3. preventDefault로 이벤트 발생 후 동작을 막음 / 여기선 페이지 넘어가는 것
    // 4. 이벤트 함수 내에서 this는 아무 것도 가르키기 않는다.
    // 5. 함수에 bind 값을 해줘서 새로운 함수로 만들어주는 느낌
    // 6. 
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
    ```

  - 위 코드처럼 state값을 변경 시키려면 this.state.mode = 'welcome' 처럼 하는게 아니라 setState 함수를 불러와서 변수를 재할당해주어야한다.



#### 7. Component event

- 예시

  - ```react
    //App.js
    // 함수도 prop이 가능!
    <Subject 
      title={this.state.subject.title}
      sub={this.state.subject.sub}
      onChangePage={function(){
        this.setState({mode:'welcome'});
      }.bind(this)}
    ></Subject>
    
    //Subject.js
    //...
    return (
      <header>
        <h1><a href="/" onClick={function(e){
          e.preventDefault();
          this.props.onChangePage();
        }.bind(this)}>{this.props.title}</a></h1>
        {this.props.sub}
      </header>
    );
    //...
    ```

- id를 자식에서 부모한테 주는 방법

  - ```react
    // 자식
    // 첫번째 방법
    <li key={data[i].id}>
      <a 
        href={"/content/" +data[i].id}
        data-id={data[i].id} // 좌측의 방식으로 a 태그에 id라는 속성을 준다.
        onClick={function(id, num, e){
          e.preventDefault()
          this.props.onChangePage(e.target.dataset.id); // e에서 받은 id값을 부모한테 전달한다.
        }.bind(this, data[i].id, 10)}
      >{data[i].title}</a>
    </li>);
    
    // 두번째 방법
    <li key={data[i].id}>
      <a 
        href={"/content/" +data[i].id}
        onClick={function(id, num, e){
          e.preventDefault()
          this.props.onChangePage(id); // 2. 함수의 인자를 id로 부모한테 전달한다.
        }.bind(this, data[i].id, 10)} // 1. bind 인자에 id 값을 주고 onclick 함수에 인자로 앞에서부터 던져준다.
      >{data[i].title}</a>
    </li>);
    ```

##### props vs state

![image-20220115164811125](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220115164811125.png)

- props는 사용은 가능하나 수정은 안됨
- state는 사용도 가능하고 this.setState를 사용하여 수정도 가능
- 둘 다 render를 호출함
- 상위 -> 하위 컴포넌트에게는 props로 값을 전달! 하위 -> 상위 컴포넌트는 event로 값을 전달! 







##### class 방식의 component

- constructor()
  - 생성자, component가 생성될 때 가장 먼저 호출되는 메서드
  - super()를 호출한다.
  - this.state = {}; 로 state값 할당 가능 (객체 리터럴)

