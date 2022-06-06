package com.example.jpa.bookmanager.repository;

import com.example.jpa.bookmanager.domain.User;
import org.springframework.data.domain.Sort;
import org.springframework.data.jpa.repository.JpaRepository;

import java.time.LocalDateTime;
import java.util.List;
import java.util.SortedMap;

public interface UserRepository extends JpaRepository<User, Long> {
    List<User> findByName(String name);

    User findByEmail(String email);

    User getByEmail(String email);

    User readByEmail(String email);

    User queryByEmail(String email);

    User searchByEmail(String email);

    User streamByEmail(String email);

    User findUserByEmail(String email);

    List<User> findUserByNameAndEmail(String name, String email);

    List<User> findByCreatedAtAfter(LocalDateTime yesterday);

    List<User> findByIdAfter(Long id);


    List<User> findByNameIn(List<String> names);

    List<User> findTop1ByNameOrderByIdDesc(String name);

    List<User> findFirst1ByNameOrderById(String name);

    List<User> findFirst1ByNameOrderByIdDescEmailAsc(String name);

    List<User> findFirstByName(String name, Sort sort);
}
