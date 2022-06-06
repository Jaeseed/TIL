package com.example.jpa.bookmanager.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class WebController {
    @GetMapping(value = "/test")
    public String main() {
        return "index";
    }
}
