package hello.hellospring;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class HelloSpringApplication {

	public static void main(String[] args) {
		// tomcat이란 웹서버를 띄우면서 같이 실행
		SpringApplication.run(HelloSpringApplication.class, args);
	}

}
