## Function으로 component 정의

#### 1. function component 정의

예시

```react
function FuncComp(props) {

  return (
    <div className='container'>
    </div>
  );
}
```



#### 2. useState

- useState: state를 관리

- useState는 기본으로 상태값, 상태를 변화시키는 함수를 가지며 useState() <= 여기서 괄호 안의 값이 state의 값이다.





##### Class에서의 라이프 사이클

- ![React component lifecycle, API 정리 · React](https://gseok.gitbooks.io/react/content/assets/react-life-cycle-2.png)



#### 3. useEffect

- 





##### render 2번 실행 되는 기능 참고

- index.js의 <React.StrictMode>가 render를 2번 실행하게 만든다.
- 개발 단계에서만 작동하고 버그를 좀 더 일찍 잡을 수 있게 도와준다.
- 위 <React.StrictMode> 코드 삭제 후 서버 실행하면 해결 됨!





#### 더 알아볼 내용

- api 가져오기 -> fetch
- static: component 내에 메서드 생성
- class 에서의 life cycle
- function에서의 hook