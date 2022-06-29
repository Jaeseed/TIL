package com.example.demo.controller;


import com.example.demo.dto.User;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api")
public class ApiController {

    @GetMapping("/text")
    public String text(@RequestParam String account) {
        return account;
    }

    @PostMapping("/json")
    public User json(@RequestBody User user) {
        return user;
    }

    @PutMapping("/put")
    public static ResponseEntity<User> put(@RequestBody User user) {

        return ResponseEntity.status(HttpStatus.CREATED).body(user);
    }
}