package com.example.jpa.bookmanager.repository;

import com.example.jpa.bookmanager.domain.Gender;
import com.example.jpa.bookmanager.domain.User;
import org.assertj.core.util.Lists;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.data.domain.*;

import javax.transaction.Transactional;

import java.time.LocalDateTime;

import static org.junit.jupiter.api.Assertions.*;
import static org.springframework.data.domain.ExampleMatcher.GenericPropertyMatchers.contains;
import static org.springframework.data.domain.ExampleMatcher.GenericPropertyMatchers.endsWith;

@SpringBootTest
class UserRepositoryTest {
    @Autowired
    private  UserRepository userRepository;

    @Test
    void crud() {
        userRepository.save(new User("david","david@js.com"));

        User user = userRepository.findById(15L).orElseThrow(RuntimeException::new);
        user.setEmail("daviddd.com");

        userRepository.save(user);

    }

    @Test
    void select() {
//        System.out.println(userRepository.findByName("d"));
//
//        System.out.println("findByEmail: " + userRepository.findByEmail("daviddd.com"));
//        System.out.println("ddByEmail:" + userRepository.ddByEmail("daviddd.com"));
//        System.out.println("findUserByNameAndEmail: " + userRepository.findUserByNameAndEmail("david", "daviddd.com"));
//
//        System.out.println("findByCreatedAtAfter: " + userRepository.findByCreatedAtAfter(LocalDateTime.now().minusDays(1L)));
//        System.out.println("findByIdAfter: " + userRepository.findByIdAfter(4L));
//
//        System.out.println("findByNameIn: " + userRepository.findByNameIn(Lists.newArrayList("davi")));

        System.out.println("findFirst1ByNameOrderById: " + userRepository.findFirst1ByNameOrderById("david"));
        System.out.println("findFirst1ByNameOrderByIdDescEmailAsc: " + userRepository.findFirst1ByNameOrderByIdDescEmailAsc("david"));
        System.out.println("findFirstByName:" + userRepository.findFirstByName("david", Sort.by(Sort.Order.desc("id"))));
    }

    @Test
    void insertAndUpdateTest() {
        User user = new User();
        user.setName("js");
        user.setEmail("js@naver.com");
        userRepository.save(user);

    }

    @Test
    void enumTest() {
        User user = userRepository.findById(1L).orElseThrow(RuntimeException::new);
        user.setGender(Gender.MALE);

        userRepository.save(user);

        userRepository.findAll().forEach(System.out::println);
    }
}