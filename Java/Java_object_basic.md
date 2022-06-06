## 객체 지향 개요

##### 1) OOP(Object Oriented Programming)

- 객체마다 변수와 메서드를 가지고 있다
- 객체 간의 이동이 자유롭다



##### 2) 객체, 클래스, 인스턴스

- (1) 객체(Object)
  - 현실 세계에 존재하는 유무형의 모든 것을 의미하며, 사람들이 의미를 부여하고 분류하는 논리적인 단위를 말한다.
  - 정적인 요소 - 변수(ex/ 이름, 속도, 색깔, 제조사)
  - 동적인 요소 - 메서드(ex/ 시동켠다(), 가속한다())
- (2) 클래스(Class)
  - 자바 응용 프로그램을 구성하는 가장 기본적인 요소, 메모리 상의 객체인 인스턴스를 생성하기 위한 템플릿으로 사용
  - 현실 세계의 객체를 프로그램에서 이용할 수 있는 객체로 만들어줌
- (3) 인스턴스(Instance)
  - 객체가 컴퓨터 메모리에 올라간 것
  - 컴퓨터 메모리에 존재하는 객체
- 위 3가지의 관계
  - ![image-20220108002259414](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220108002259414.png)
  - 주로 object와 instance를 같은 용어로 사용(메모리 상에서)



##### 3) 상속과 다형성

- 상속: 기존에 있던 클래스에 변수를 추가하여 기존 클래스의 특성을 가짐

  - 코드를 간결하게 하여 재사용성을 확대할 수 있다

  - 상속을 통해 객체들 사이의 계층 구조를 이룰 수 있음(마치 트리와 비슷)

  - 부모 클래스와 자식 클래스의 예시

    ```java
    //Car.java 부모 클래스로써 Taxi 클래스에 상속함
    public class Car {
        // 멤버 변수 선언
        String name;		// 공개할 변수
        int currentGear;	// 공개할 변수
        // 메서드 선언
        void changeGear(int gear) {
            System.out.println("-> 기어를 " + gear + "단으로 변경한다.");
            currentGear = gear;
        }
        String getCurrentState() {
            return name + "의 현재 기어: " + currentGear;
        }
    }
    
    // Taxi.java 부모 클래스의 변수와 메서드를 모두 물려받음
    public class Taxi extends Car { // extends가 상속 관계 예약어
        // 요금
        int fare;
        // 승객 유무
        boolean passengerYn;
    }
    ```

  - 자식 클래스의 객체 생성

    ```java
    // CarTest.java
    public class CarTest {
        public static void main(String[] args) {
            // Car 객체(instance) 생성
            Taxi myTaxi = new Taxi();
           	
            // 초기값 설정
            // Car클래스로부터 상속된 변수
            myTaxi.name="태현운수";
            myTaxi.currentGear = 2;
            // Taxi 클래스에 추가한 변서
            myTaxi.fare = 3400;
            myTaxi.passengerYn = true;
            System.out.println(myTaxi.getCurrentState());
        }
    }
    ```

- 다형성

  - one interface, multiple implementation => 하나의 인터페이스를 이용해 서로 다른 구현을 제공함
  - 메서드 오버로딩: 한 클래스 안에 같은 이름의 메서드를 여러 개 정의하면서, 그 인자의 개수나 유형을 다르게 해 놓은 형태
  - 메서드 오버라이딩
    - 상속 관계에 있는 하위 클래스가 상위 클래스가 가지고 있는 메서드를 재정의 하는 것
    - 재정의된 메서드가 선언된 형태는 상위 클래스에서 선언된 것과 같음





### 객체 생성

- public, default, private
  - public: 은 어디에서나 쓸 수 있음
  - default: 아무 값도 없으면 자동으로 default이고 해당 패키지 내에서만 사용 가능
  - private: 해당 클래스 내에서만 사용 가능
- static: 새로운 인스턴스 생성 없이 해당 클래스에 접근 가능함
- void: return 값이 없어도 됨