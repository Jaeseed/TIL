# 2번
def solution(companies, applicants):
    answer = []
    # 회사 목록 정리
    company_dict = dict()
    # 지원자 목록 정리
    applicant_dict = dict()
    for st in companies:
        company, c_order, to = st.split()
        # 우선순위, 총 채용 수, 현재 후보
        company_dict[company] = [list(c_order), [int(to)], []]
    for st in applicants:
        applicant, a_order, cnt = st.split()
        # 우선 순위, 지망 회사 수, 진행 유무
        applicant_dict[applicant] = [a_order, int(cnt),0]
    flag = 1
    while flag:
        flag = 0
        for key, value in applicant_dict.items():
            target, num, is_cand = value
            # 지망 회사에 모두 지원했거나 현재 진행 중일 때 continue
            if num == 0 or is_cand == 1:
                continue
            flag = 1
            # 회사 채용 후보에 추가
            order_num = company_dict[target[0]][0].index(key)
            company_dict[target[0]][2].append([order_num, key])
            # 타겟 회사 제외
            applicant_dict[key][0] = applicant_dict[key][0][1:]
            # 희망 지원 회사 수 빼기
            applicant_dict[key][1] -= 1
            # 진행 유무 갱신
            applicant_dict[key][2] = 1
        for key, value in company_dict.items():
            # 총 채용 수
            now_to = value[1][0]
            company_dict[key][2].sort()
            # 총 채용 수보다 지원자가 많을 때
            if len(company_dict[key][2]) > now_to:
                for idx in range(now_to, len(company_dict[key][2])):
                    # 지원자 진행 유무 초기화
                    this_app = company_dict[key][2][idx][1]
                    applicant_dict[this_app][2] = 0
                # 슬라이싱
                company_dict[key][2] = company_dict[key][2][:now_to]
    for key, value in company_dict.items():
        # 최종 합격자 리스트
        employee = ''
        # 합격자 명 오름차순 정렬
        value[2].sort(key=lambda x:x[1])
        for v in value[2]:
            employee += v[1]
        answer.append(key + '_' + employee)
    return answer
solution(["A abc 2", "B abc 1"], ["a AB 1", "b AB 1", "c AB 1"])
