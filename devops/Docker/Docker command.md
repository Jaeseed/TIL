# Docker command

- none images 삭제
  - docker rmi $(docker images -f "dangling=true" -q)
- 모든 docker container 종료
  - docker stop $(docker ps -a -q)

- 모든 docker container 삭제
  - docker rm -f $(docker ps -aq)
- 모든 docker image 삭제
  - docker rmi $(docker images -q)




<img src="C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220326112055174.png" alt="image-20220326112055174" style="zoom:200%;" />




