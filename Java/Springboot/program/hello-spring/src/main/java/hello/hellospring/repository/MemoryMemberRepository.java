package hello.hellospring.repository;

import hello.hellospring.domain.Member;
import org.springframework.stereotype.Repository;

import java.util.*;

@Repository
public class MemoryMemberRepository implements MemberRepository {
    // alt+enter: implememts method 만들 수 있음

    private static Map<Long, Member> store = new HashMap<>();
    // sequence는 id를 생성하는 거라고 생각하면 간단
    private static long sequence = 0L;
    // override는 기존 값을 덮어쓴다는 뜻
    @Override
    public Member save(Member member) {
        member.setId(++sequence);
        store.put(member.getId(), member);
        return member;
    }

    @Override
    public Optional<Member> findById(Long id) {
        // Optional.ofNullable하면 값이 없어도 해결 됨
        return Optional.ofNullable(store.get(id));
    }

    @Override
    public Optional<Member> findByName(String name) {
        return store.values().stream()
                .filter(member -> member.getName().equals((name)))
                .findAny();
    }

    @Override
    public List<Member> findAll() {
        return new ArrayList<>(store.values());
    }

    public void clearStore() {
        store.clear();

    }
}
