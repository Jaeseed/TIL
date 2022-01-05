## Jira & JQL

#### Issue Tracking

- 팀의 할 일을 관리
- 각 issue마다 상태를 지정해놓고 관리함



#### Project Management

- 메모 못함..



#### Agile

- 알아보기



####  Scrum VS Kanban

- Scrum: 스프린트를 생성, 
- Kanban: 담당자별로 할 일을 할당해줌





####  DevOps

- Dev: development, ops: operations

![image-20220105102416109](C:\Users\Jaesung\AppData\Roaming\Typora\typora-user-images\image-20220105102416109.png)

- CI/CD란 무엇인가?
- DevOps를 잘 수행하기 위한 조건
  - 반복적인 작업들을 Tool을 이용해서 자동화
  - 팀원 모두가 알고 있는 하나의 공유된 지표가 필요
  - 장애나 이슈가 있을 때 혼자만 알지 말고 팀원들과 공유 필요



#### Atlassian?



#### SRE(Site Reliability Engineering)

- 짤막 정보
  - 신뢰성: ex) 우리는 일주일에서 1시간 이내의 신뢰성을 주겠다 => 일주일에 장애를 1시간 안으로 하겠다.
  - 가용성: 놓침





#### Jira 이슈 생성!

- issue type
  - story: 시나리오
  - task: 각자 할 일 등록 / story와 크게 구분 안 될 때도 있음
  - bug: 버그 관련 일 등록
  - epic: 큰 틀을 나누는 항목, 위 3가지 type의 상위 형식인 것 같다.
- summary: issue 제목
- component: epic이랑 비슷한 느낌인 것 같다.
- Fix Version: 말 그대로 버전
- labels: 형식에 제한 없이 꼬리말 같은 느낌
- linked issues: 관련 있는 issue 
- sprint: 1주차 2주차처럼 시간 단위로 나눈 개발 계획인 듯



#### Filter

- 원하는 필터로 거른 후의 issue들을 모을 수 있는 메뉴를 생성할 수 있다.



#### JQL

- Jira Query Language
- Jira Issue를 구조적으로 검색하기 위해 제공하는 언어
- Jira Issue 검색 시 사용할 수 있는 언어 ex) resolved = unresolved



#### Dashboard

- 가젯이 무엇인가 => 대쉬보드 안의 카드 모양으로된 각각의 항목인 듯



*Jira에는 plugin이 많다고 한다. plugin이 뭘까?



#### *Tip

- 이슈를 나눌 땐 규칙적으로 나누는게 좋다
- 이슈를 예전엔 티켓이라고 부르기도 했음
- 추천 플러그인: Scriptrunner
  - Jira에 대한 지식이 있어야 활용할만함