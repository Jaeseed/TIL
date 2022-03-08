# Docker

#### Dockerfile

- FROM으로 시작
- RUN: 실행할 명령어 ( 하나로 연결하는 것을 권고함 ex)RUN apt update && apt install -y python3)
  - &&: 앞에 있는 것부터 순서대로 설치 됨
  - -y: 자동으로 y를 누르는 yes 명령어
- WORKDIR: 디렉토리 생성
- build  
  - ex) docker build -t 이름 ( -t: tag)
  - ==> 이미지 생성 됨
- RUN과 CMD의 차이
  - RUN은 빌드가 되는 시점(이미지에 반영)
  - CMD는 컨테이너가 실행될 때(컨테이너에 반영)

```dockerfile
FROM ubuntu:20.04
RUN apt update && apt install -y python3
WORKDIR /var/www/html
# 이후엔 WORKDIR에서 진행 됨
RUN echo "HELLO, <strong>DOcker></strong>" > index.html # index.html에 해당 글 저장
COPY ["index.html", "."] # 왼쪽 호스트의 파일을 오른쪽 "."경로(현재 경로)에 복사하는 것
CMD ["python3", "u", "-", "http.server"]
```



#### Docker compose

- 파일명: docker-compose.yml
- 생성 시 자동으로 네트워크 생성되고 compose 내에 서버들끼리 네트워크를 공유함

```dockerfile
version: "3.7" # docker compose 버전
services: # 만들고 싶은 컨테이너 목록
	db: # 컨테이너 이름
		image: mysql:5.7 # 이미지 생성
		volume: # 데이터를 호스트에 저장
			-./db_data:/var/lib/mysql # 왼쪽(컨테이너), 오른쪽(로컬) 연결
        environment:
        	MYSQL_ROOT_PASSWORD: 123456 # 환경
   	app:
   		depends_on: # 먼저 설치될 이미지를 지정
   			-db
   	ports:
   		-"8080:80"
```

