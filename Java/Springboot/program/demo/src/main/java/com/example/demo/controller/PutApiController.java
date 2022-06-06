package com.example.demo.controller;

import com.example.demo.dto.PostRequestDto;
import com.example.demo.dto.PutRequestDto;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api")
public class PutApiController {

    @PutMapping("/put/{userId}")
    public PutRequestDto put(@RequestBody PutRequestDto requestDto, @PathVariable(name = "userId") Long id) {

        System.out.println(requestDto);
        return requestDto;
    }
}
