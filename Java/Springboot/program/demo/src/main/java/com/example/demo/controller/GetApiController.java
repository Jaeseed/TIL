package com.example.demo.controller;


import com.example.demo.dto.UserRequest;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

@RestController
@RequestMapping("/api/get")
public class GetApiController {

    @GetMapping(path="/hello")
    public String hello() {
        return "get hello";
    }

    @RequestMapping(path="/hi", method = RequestMethod.GET)
    public String hi() {
        return "hi";
    }

    // path variable 사용법
    @GetMapping("/pathVariable/{name}")
    // 아래와 같은 방식으로 pathVarible과 다른 이름의 변수를 받을 수 있음
//    public String pathVariable(@PathVariable(name = "name") String pathName, String name)
    public String pathVariable(@PathVariable String name){
        System.out.println("PathVariable: "+name);
        return name;
    }

    // query-param?user=steve&email=steve@gmail.com...
    @GetMapping("query-param")
    public String queryParam(@RequestParam Map<String, String> queryParam) {

        StringBuilder sb = new StringBuilder();
        queryParam.entrySet().forEach( entry -> {
            System.out.println(entry.getKey());
            System.out.println(entry.getKey());
            System.out.println("\n");

            sb.append(entry.getKey()+" = "+entry.getValue()+"\n");
        });

        return sb.toString();
    }

    @GetMapping("query-param02")
    public String queryParam02(
            @RequestParam String name,
            @RequestParam String email,
            @RequestParam int age
    ){
        return name+" "+email+" "+age;
    }

    @GetMapping("query-param03")
    public String queryParam03(UserRequest userRequest) {

        System.out.println(userRequest.getName());
        System.out.println(userRequest.getEmail());
        System.out.println(userRequest.getAge());

        return userRequest.toString();
    }
}
