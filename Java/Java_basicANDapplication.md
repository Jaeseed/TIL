## Java 기본 및 응용

##### Garbage Collection(G.C)

- 자바의 특징 중 하나로 더 이상 사용하지 않는 메모리를 자동으로 정리하는 기능
- java에서 기본적으로 제공하는 기능

```java
// 짤막 상식
String hello = new String("Hello");
// 위에서 new는 새로운 객체를 메모리에 담는 예약어
```



##### CLI 환경에서 컴파일 & run

- compile: C:\tmep>javac -d . 파일명.java
- run: C:\temp>java 패키지명.파일명(java 확장자명 필요 x)



##### workspace 바꿀 때마다 encoding을 UTF-8로 설정하자

- eclipse.ini 파일 밑에 명령어 추가하여 default 값을 UTF-8로 할 수 있다



##### perspective

- 하단의 markers, properties 등등을 perspective라고 함



##### 객체지향

- 객체: 멤버 변수, 메서드를 가진다.
- . --> ~~ 가 가지고 있는~ 로 읽어도 좋겠다.



##### Java API(java documentation)

- http://docs.oracle.com/javase/8/docs/api/index.html?overview-summary.html



##### Type

- 변수에 저장되는 데이터의 종류
- Primitive Type(기본형)
  - 미리 정해진 크기의 Memory Size로 표현
  - 변수 자체에 값 저장
- Reference Type(참조형)
  - 미리 정해질 수 없는 데이터의 표현
  - 변수에는 실제 값을 참조할 수 있는 주소만 저장



##### Primitive Type

- 정수형은 주로 int(32), 실수형은 주로 double(64) 사용



##### 예약어 final

- 변수에 더 이상 값을 할당할 수 없게 마지막으로 선언함(상수)
- ex) final int i = 0;
- final 변수는 'final int i;' 로 blank 상태로 선언 가능



##### 형변환

```java
{
    int i = 10;
	byte b = i;
}
// int의 32비트 크기를 byte의 8비트 크기에 할당할 수 없기에(집 크기가 다름) 명시적 형변환을 해야한다. 
// ex) byte b = (byte) i;
{
    byte b = 10;
    int i = b;
}
// 가능
```

- primitive는 primitive끼리, reference는 reference끼리 형 변환 가능
  - boolean은 다른 기본 타입과 호환 불가능
- 형변환 연산자
  - 명시적 형변환: 괄호 사용
    - ex) int result = (int)d;
  - 묵시적 형변환
    - 타입의 표현 범위가 커지는 방향으로 할당할 경우는 묵시적 형변환 발생(int보다 실수가 훨씬 표현 범위가 크다)
    - ex) byte b = 10; int i = (int)b; int i2 = b;
- 작 은집 -> 큰 집 : 손실 없음 / 큰 집 -> 작은 집: 손실 있음



##### 퀴즈

```java
// 틀린 변수 선언을 찾으시오
public static void main(String[] args) {
    // 1번 자바는 기본적으로 문자열 첫 글자를 대문자로 쓴다.
    string s1 = "Hello";
    // 2번 합격
    String s2 = "Hello";
    // 3번 합격
    String s3 = new String("Hello");
    // 4번 문자열을 바로 char의 배열로 입력이 안 되는 듯
    char[] s4 = "Hello";
}
// 상수 문자열 객체를 이용하는 것(2번)이 일반 String 객체를 이용하는 방법(3번)보다 효율적
```

