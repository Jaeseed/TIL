# Ubuntu 명령어 정리

### apt

##### 주로 sudo에서 실행

- update: 설치 가능한 패키지 리스트를 최신화
- upgrade: 실제 업데이트
- list: 리스트 불러오기
- list --upgradable:  업그레이드 필요한 목록 불러 옴





### 목록 확인

- ls





### 디렉토리

#### 1. 디렉토리 생성

- mkdir [디렉토리명]
- mkdir -p [티렉토리명]/.../: 여러 디렉토리 생성



#### 2. 디렉토리 이동

- cd [명]
- cd ..: 부모 디렉토리 이동



#### 3. 디렉토리 삭제

- rm -r [디렉토리 명]





### 파일

#### 1. 빈 파일 생성

- touch [파일명]



#### 2. 파일 삭제

- rm [파일명]



#### 3. 파일 복사

- cp [파일 위치 및 파일 이름] [목적지 파일위치 및 파일 이름]



#### 4. 파일 이동(파일 이름 바꿀 때도 사용)

- mv [파일 위치 및 파일 이름] [목적지 파일위치 및 파일 이름]
- mv [원래 파일 이름] [바꾸고 싶은 파일 이름]





### vim

##### 파일 직접 접근 및 수정

- vi 파일명 또는 경로명/파일: 접근
  - q: 나가기
  - qw: 수정 후 나가기
  - qa: 수정 없이 나가기
  - !: 강제로 실행





### 심볼릭 링크 연결?





![image-20220322160735568](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220322160735568.png)