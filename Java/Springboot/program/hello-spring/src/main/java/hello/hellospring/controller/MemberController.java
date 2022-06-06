package hello.hellospring.controller;

import hello.hellospring.domain.Member;
import hello.hellospring.service.MemberService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import java.util.List;

// spring 시작 시 controller 객체를 생성하고 spring이 관리함
@Controller
public class MemberController {

    private final MemberService memberService;

    // 세터 주입 final 없어야 함
//    @Autowired
//    public void setMemberService(MemberService memberService) {
//        this.memberService = memberService;
//    }

    // memberService를 container의 memberService와 연결 시켜줌 (depency injection)
    @Autowired
    // 생성자 주입 - 가장 선호하는 방식
    public MemberController(MemberService memberService) {
        this.memberService = memberService;
    }

    // 필드 주입
    // @Autowired private MemberService memberService;

    @GetMapping("/members/new")
    public String createForm() {
        return "members/createMemberForm";
    }

    @PostMapping("/members/new")
    public String create(MemberForm form) {
        Member member = new Member();
        member.setName(form.getName());

        memberService.join(member);

        return "redirect:/";
    }

    @GetMapping("/members")
    public String list(Model model) {
        List<Member> members = memberService.findMembers();
        model.addAttribute("members", members);
        return "members/memberList";
    }
}
