# Redux

#### 리덕스의 구조



![image-20220202010616309](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220202010616309.png)

- state
  - state로의 직접 연결은 불가
- reducer
  - state를 조작하는 함수
  - action에서 가져 온 데이터와 state를 이용해 새로운 state의 값을 생성
- render
  - UI를 만들 개발자가 만들 코드
- getState
  - state를 가져올 때는 getState를 사용해야한다.
- subscribe
  - ex) store.subscribe(함수); 를 하면 state의 값이 바뀔 때마다  함수를 render 해준다
- action
  - dispatch 명령어를 사용해서 값을 전달함
  - type이 필요 ex) 'create'
- dispatch
  - 현재의 state와 



#### redux 설정

- 설치: npm install --save redux

- store 생성

  - ```react
    function reducer(state, action) {
      if (state === undefined) {
        return {color:'yellow'} // return 값을 state에 넣음
      }
      if (action.type === 'CHANGE_COLOR'){
        state.color = 'red' // 좌측처럼 state를 직접 변경 후 리턴하는 방식은 비추천
        var newState = Object.assign({}, state, {color:'red'}); // 좌측처럼 newState를 이용해 return 하는 것을 추천
      } 
      return newState;
    }
    
    var store = Redux.createStore(reducer, 시간여행 코드 / docu 참고 );
    store.subscribe(red); // store의 값이 바뀔 때마다 red 함수를 호출
    ```

- state 가져오기

  - store.getState();

- action 사용

  - ```react
    store.dispatch({type:'CHANGE_COLOR', color: 'red'}); // type이 필수! 뒤에 데이터 값도 필요!
    ```





##### 팁

- Object.assign({}, {name: 'egoing'}, {city: 'seoul'}); -> 첫번째 인자 {}에 오른쪽 값들을 복사
  - 추가하려는 값들의 키 값과 같은 값이 있으면 변경이고 없으면 단순 추가인 것 같다.
- 배열 복사는 concat을 사용 ex) state.content.concat(); // concat 안에 정수를 넣으면 slicing 같은 느낌인 듯
- immutable이 무엇인가
- input 태그의 정보를 가져올 때 this.name.value 를 이용해 해당 name을 가진 input 태그의 값을 가져올 수 있다.