## 라우터

#### 1. 공식문서

- react router 검색하면 뜸(v6로 업데이트 되며 DOCS 새로 생겼으니 주의할 것)
- [공식 문서 페이지](https://reactrouter.com/)



#### 2. 설치

- npm install react-router-dom



#### 3. 라우터 선언

- 라우터를 만들 js파일 내에 import {BrowserRouter} from 'react-router-dom' 임포트

- 라우터를 만들 component를 BrowserRouter태그로 덮는다

- ##### 만약 사용자가 잘못된 라우터에 접근한다면 어떻게 해야할까? v6엔 exact, switch가 안 먹힌다.

- a 태그로 하면 페이지가 재로딩이 되지만 link를 import해서 태그로 쓰고 경로엔 to="/" 와 같은 방식으로 등록하면 SPA 처럼 움직인다.

#### 

#### 4. 라우터 메서드

- BrowserRouter
- Routes
- Route
- Link
- Outlet

- NavLink
  - Link와 거의 같다
  - Link와는 달리 NavLink는 active라는 class가 생긴다.
  - css로 현재 active인 라우트에 배경색을 줄 수도 있다.





#####  경로 '*'

- 다른 경로가 일치하지 않을 경우에만 일치하는 예외 처리 url

- ```react
  // 아래와 같은 방식으로 사용
  <Route
  path="*"
  element={
    <main style={{ padding: "1rem" }}>
      <p>There's nothing here!</p>
    </main>
  }
  />
  ```





##### HashRouter

- 뭔지 잘 모르겠음







#### 5. 매개변수 읽기

- ```react
  // 아래와 같은 방식으로 매개변수 주기 ex) :invoiceId
  <Route path="invoices" element={<Invoices />}>
    <Route path=":invoiceId" element={<Invoice />} />
  </Route>
  ```



#### 6. 인덱스 라우트

- ```react
  <Route
  index
  element={
    <main style={{ padding: "1rem" }}>
      <p>Select an invoice</p>
    </main>
  }
  />
  ```

- 인덱스 경로가 빈 공간을 채움! 상위 경로를 인덱스 경로가 굥유하기 때문이다. 경로는 따로 없다.

- 인덱스 경로는 상위 경로의 경로에 있는 상위 경로 콘센트에서 렌더링된다.

- 인덱스 경로는 상위 경로가 일치하지만 다른 하위 경로는 일치하지 않을 때 일치합니다.

- 인덱스 경로는 상위 경로의 기본 하위 경로입니다.

- 인덱스 경로는 사용자가 탐색 목록의 항목 중 하나를 아직 클릭하지 않은 경우 렌더링됩니다.
