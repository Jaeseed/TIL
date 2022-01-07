## Java 입문

#### 1. 자바 언어의 특징

![image-20220107174632162](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220107174632162.png)

- 자바는 단순하다.
- 자바는 객체지향적이다.
- 자바는 분산 처리에 용이하다.
- 자바는 인터프리터에 의해 실행됨
  - 소스코드- .java => 컴파일 => 중간코드- .class => 기계어로 해석 => 실행
- 자바는 견고하다.
  - 포인터 사용X
  - 자동으로 가비지 컬렉션 기능을 수행
  - 데이터 타입 검사
- 자바는 안전하다.
  - 컴파일 시에 엄격하게 데이터 타입을 검사하여 프로그램 실행 시 발생할 수 있는 비정상적인 상황을 미리 방지
- 자바는 플랫폼 독립적이다.
  - 사용하는 운영체제나 cpu 등의 하드웨어 사양에 관계 없이 실행될 수 있음
- 자바는 높은 성능을 제공한다.
  - 가비치 컬렉션 기능이 추가되어 있어 자동으로 메모리 관리가 가능하다.
- 자바는 멀티스레드를 지원한다.
- 자바는 동적이다.
  - 변화되는 환경에 잘 적응되도록 설계됨
  - 기존의 프로그램에 영향을 주지 않고, 라이브러리에 새로운 메서드나 속성을 추가할 수 있음



#### 2. 자바 플랫폼의 종류

- Java SE(Java 2 Platform Standard Edition)
  - 가장 기본이 되는 에디션, 자바 언어 대부분의 패키지 포함
- java EE(Enterprise Edition)
  - 현업에서 사용되는 API들이 집약된 에디션
- Java ME(Micro Edition)
  - 모바일 기기 등에서 사용되는 API가 포함된 에디션

##### 자바 가상 머신

![image-20220107175806174](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220107175806174.png)



##### API

Application Programming Interface



#### 3. Java 실행

- eclipse에서 실행
- 새 프로젝트 생성: file -> new -> Java Project
- source 파일 생성(src)
  - src 오른마우스 클릭 -> new -> Class
  - package는 일단 생략
  - name 설정
  - 젤 하단 public static void main(String[] args) 체크

![image-20220107221615560](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220107221615560.png)

![image-20220107221649910](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220107221649910.png)

![image-20220107221832562](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220107221832562.png)

![image-20220107221900215](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220107221900215.png)

- main method를 생성하려면 main 친 후 ctrl + space + enter 누르면 됨 또는 Class 생성 시 설정



![image-20220107223156379](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220107223156379.png)

##### 식별자 생성 규칙

- 첫 문자는 대문자 or 소문자 알파벳, _, $, 유니코드로 시작
- 특수문자 사용 불가
- 대소문자 구별, 길이 제한 x
- 예약어 포함 가능 but 예약어만 사용 x
  - 예약어는 시스템 일정 특성을 가진 언어, 데이터 타입이나 프로그램 정의를 위해 사용됨
  - 모든 예약어는 소문자!
  - ![image-20220107223448625](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220107223448625.png)
  - sizeof도 java에서 사용하지 않음
- 숫자 사용 가능, 첫 문자에는 숫자 사용 불가
- 관례상 클래스명은 대문자, 메시드 & 변수 & 상수는 소문자로 시작



##### 짤 정보

bit와 byte

![image-20220107223635364](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220107223635364.png)

##### 기본 데이터 타입의 종류

![image-20220107223708579](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220107223708579.png)

- 논리형
  - python 처럼 false를 0으로 인식 안 하는 듯

![image-20220107223743499](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220107223743499.png)

- 문자형
  - 2byte
  - 홑따옴표('') 안에 넣어야 한다.
  - 특수문자
    - ![image-20220107223935139](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220107223935139.png)

- 정수형
  - ![image-20220107224028225](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220107224028225.png)
  - 형을 명시하지 않으면 기본으로 int로 먹음
- 실수형
  - ![image-20220107224151802](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220107224151802.png)
  - 명시 안 하면 기본으로 double(ex)10.0)
- 형변환

```
ex) int i1 = 128
	b1 = (bite) i1;
	c1 = (char) i2;(유니코드)
```



#### 4. 자바 연산자

##### 1) 산술 연산자

- 정수, 실수, 사칙연산
- ![image-20220107224622304](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220107224622304.png)

- ![image-20220107224703111](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220107224703111.png)
- ![image-20220107224740553](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220107224740553.png)
- ![image-20220107224907447](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220107224907447.png)이미지처럼 int로 처음에 선언을 해주어야 하는가?



##### 2) 비교 연산자

- 파이썬과 같다
- instanceof: a instanceof b => a가 b 데이터 타입의 객체인 경우 true



##### 3) 논리 연산자

- & 는 and와 같다 // &&는 좌항이 false면 우항 실행 없이 false 리턴
- |는 or과 같다 // ||는 좌항이 true면 우항 실행 없이 true 리턴
- ! (ex) !a) 값이 true면 false로, false면 true로 변경!



##### 4) 비트 연산자

- ![image-20220107225627935](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220107225627935.png)



##### 5) 대입 연산자

- =
- ![image-20220107225754150](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220107225754150.png)



##### 5) 조건 삼항 연산자

- 변수 = 조건 ? 값1 : 값2
  - 조건이 참이면 값1이 변수에 대입, 거짓이면 값2가 변수에 대입
- ![image-20220107225901684](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220107225901684.png)



#### 6. 자바 배열

##### 1) 1차원 배열

- ![image-20220107230132458](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220107230132458.png)
- ![image-20220107230152896](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220107230152896.png)![image-20220107230225536](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220107230225536.png)
- 배열 변수명.length -> 배열의 길이를 알 수 있음
- 배열변수명[인덱스번호] -> 인덱스 번호 조회 (인덱스는 0부터 시작)



##### print 관련 짤막 상식

- print / printf / println의 차이

![image-20220107231038461](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220107231038461.png)

- println(3 + "냠 "); 하면 3냠이 출력되는 신기한 비밀 



##### 2) 이차원 배열

- 선언방식
  - ![image-20220107231156327](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220107231156327.png)
- 배열 객체 생성
  - ![image-20220107231230056](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220107231230056.png)![image-20220107231258990](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220107231258990.png)
- 



##### 명령형 매개변수

- ![image-20220107231653511](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220107231653511.png)
- ![image-20220107231814625](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220107231814625.png)

- 명령형 매개변수는 python의 input과 비슷한 듯?
  - ![image-20220107232207513](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220107232207513.png)
- 사용법 !!
  - run as에서 run configurations 클릭
  - arguments에 명령형 매개변수 입력! (스페이스로 구분됨)





#### 7. 제어문

##### 1) 조건 제어문

- 개요
  - ![image-20220107232657627](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220107232657627.png)
  - if & else => if else와 같음
  - if & else if & else => if elif else와 같음
- switch
  - ![image-20220107233230142](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220107233230142.png)
  - ![image-20220107233247418](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220107233247418.png)
  - break가 없으면 switch 블록이 끝날 때까지 다음 case문에 대한 문장을 차례대로 수행



##### 2) 반복 제어문

- 종류
  - for, while
    - 조건에 따라 수행 안 될 수도 있음
  - do-while
    - 무조건 한 번 이상 수행됨
- 반복 제어문은 조건식을 포함해야함
  - for, while문에 사용되는 조건식의 연산 결과는 true 또는 false를 사용함
- for
  - ![image-20220107233629385](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220107233629385.png)
  - 조건식이 false일 때까지 시행 됨
  - for 블록 내 선언 변수는 for 블록 내부에서만 사용 가능
  - for 블록을 포함하는 method 내에서 선언된 변수와 같은 이름으로 선언 불가
  - ![image-20220107233747518](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220107233747518.png)
- while
  - ![image-20220107234012236](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220107234012236.png)
- do-while
  - do 블록을 한번 수행한 후에 while 조건식을 판단하는 구조
  - ![image-20220107234155504](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220107234155504.png)



##### 3) 이동 제어문

- break, continue, return(메서드의 수행 종료하고 호출된 곳으로 제어를 이동 시킴)
- Lable을 사용하면 break와 continue가 원하는 곳으로 이동
  - 예시![image-20220107234625387](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220107234625387.png)
  - ![image-20220107234715024](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220107234715024.png)

