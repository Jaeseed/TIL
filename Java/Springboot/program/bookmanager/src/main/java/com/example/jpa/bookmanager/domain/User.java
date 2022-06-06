package com.example.jpa.bookmanager.domain;

import lombok.*;

import javax.persistence.*;
import java.time.LocalDateTime;

// getter, setter 따로 명명 안 해도 됨
// 아래는 클래스 scope으로 선언한거고 필드 scope으로 각각 선언해주어도 됨
//@Getter
//@Setter
// Lombok에서 ToString 을 알아서 해줌
//@ToString
// 인자 없이 생성함 ex) User user = new User();
@NoArgsConstructor

//User user1 = new User("martin", "martin@fa.com", LocalDateTime.now(), LocalDateTime.now()); 처럼 쓸 수 있음
@AllArgsConstructor
@RequiredArgsConstructor
//Equivalent to @Getter @Setter @RequiredArgsConstructor @ToString @EqualsAndHashCode.
@Data
@Builder
@Entity
@Table(indexes = { @Index(columnList = "name")}, uniqueConstraints = {@UniqueConstraint(columnNames = {"email"})})
public class User {
    @Id
    // 자동으로 1씩 값이 증가함
    @GeneratedValue
    private Long id;
    @NonNull
    private String name;
    @NonNull
    private String email;

    @Enumerated(value = EnumType.STRING)
    private Gender gender;

    @Column(updatable = false)
    private LocalDateTime createdAt;

    private LocalDateTime updatedAt;

    // DB에 반영 되지 않음
    @Transient
    private String testData;

    // pre는 이전 post는 직후에 작동
//    @PrePersist
//    @PreUpdate
//    @PreRemove
//    @PostPersist
//    @PostUpdate
//    @PostRemove
//    @PostLoad


}
