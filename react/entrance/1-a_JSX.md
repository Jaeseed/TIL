## JSX

#### JSX란?

- react에선 본질적으로 렌더링 로직과 UI 로직이 연결된다.
- JavaScript를 확장한 문법으로 JavaScript의 모든 기능이 포함 되어 있다.
- React 엘리먼트를 생성한다.



#### JSX의 표현식

- 예시

  - ```react
    // 1. 
    const element = <h1>Hello, {name}</h1>;
    // 위처럼 JSX의 중괄호 안에는 유효한 모든 JavaScript 표현식을 넣을 수 있다. 변수는 물론 함수도 가능!
    
    // 2.
    const element = <img src={user.avatarUrl} />;
    // 태그가 비어있다면 XML 처럼 />로 닫아줘야 한다.
    
    // 3.
    const element = (
      <div>
        <h1>Hello!</h1>
        <h2>Good to see you here.</h2>
      </div>
    );
    // JSX 태그는 자식을 포함할 수 있다.
    ```

- JSX도 표현식이다.



#### JSX 객체 표현

- Babel은 JSX를 React.createElement() 호출로 컴파일 한다.

- ```react
  // 1.
  const element = (
    <h1 className="greeting">
      Hello, world!
    </h1>
  );
  
  // 2.
  const element = React.createElement(
    'h1',
    {className: 'greeting'},
    'Hello, world!'
  );
  // 위 두 예시는 같은 기능을 한다.
  ```

  



##### 짤막 상식

- 리터럴
  - 코드 상에서 데이터를 표현하는 방식
  - 변수나 상수가 메모리에 할당된 '공간'이라면 리터럴은 이 공간에 저장되는 '값'이다.