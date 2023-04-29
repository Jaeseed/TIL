# Web

- HTTP: Hypertext Transfer Protocol
- URI: Uniform Resource Identifier
  - 리소스 식별자
- HTML: Hyper Text Markup Language





### 1. REST

- Representational State Transfer, 자원의 상태 전달



#### 1) 규약

- Client, Server가 서로 독립적으로 분리 되어 있어야 한다.
- 요청에 대해서 클라이언트의 상태를 서버에 저장하지 않는다.(Stateless)

- 클라이언트는 서버의 응답을 Cache(임시 저장) 할 수 있어야 한다. 클라이언트가 Cache를 통해 응답을 재사용 할 수 있어야 하며 이를 통해 서버 부하를 낮춘다.
- 서버와 클라이언트 사이에 방화벽, 게이트웨이, 프록시 등 계층 형태로 구성 및 확장이 가능해야 한다.
- 인터페이스의 일관성을 지키고 아키텍처를 단순화시켜 작은 단위로 분리하여 클라이언트, 서버가 독립적으로 개선 될 수 있어야 한다.
- 특정한 기능을 서버로부터 클라이언트가 전달 받아 코드를 실행할 수 있어야 한다.



#### 2) RESTful

- 자원의 식별
  - 리소스 접근 시에 URI를 사용
- 메시지를 통한 리소스 조작
  - 리소스 조작을 위해 데이터 전체를 전달하는 것이 아니라 리소스의 표현으로 전달한다.
- HTTP method를 담아 표현
- 리소스에 대한  Link 정보도 같이 포함되야 한다.
  - 요녀석은 불필요한 데이터 흐름 때문에 현업에서 잘 안 쓰기도 함



### 2. URI

#### 1) URI(Uniform Resource Identifier)

- 인터넷에서 특정 자원을 나타내는 주소 값. 해당 값은 유일하며 응답은 달라질 수도 있다.



#### 2) URL(Uniform Resource Locator)

- 인터넷 상에서의 자원, 특정 파일이 어디에 위치하는지 식별하는 주소



##### *URL은 URI의 하위 개념



#### 3) URI 설계 원칙 (RFC-3986)

- 슬래시(/) 구분자는 계층 관계를 나타낼 때 사용
- URI 마지막에 슬래시하지 않음
- 하이픈(-)은 가독성을 높이기 위해 사용, 밑줄(_)은 지양
- URI 경로는 소문자가 적합
- 파일 확장자를 URI에 포함하지 않는다.
- 프로그래밍 언어에 의존적인 확장자를 사용하지 않는다.
- 구현에 의존적인 경로를 사용하지 않는다.
- 세션 ID, method명 이용 X
- 명사에 단수형 보다는 복수형 사용
- 컨트롤러 이름으로는 동사나 동사구를 사용
- variable router는 유일한 personal key를 사용
- CRUD 기능을 URI에 명시하지 않는다.
- api-jaesung 또는 dev-jaesung처럼 서브 도메인은 차이를 둔다.



### 3. HTTP

![image-20230429231125143](C:\Users\Jaesung\AppData\Roaming\Typora\typora-user-images\image-20230429231125143.png)

- 위의 사진은 HTTP method 별 특징을 정리해 놓은 표다
- 출처: 패스트 캠퍼스 Java/Spring 웹 개발 마스터 초격차 패키지