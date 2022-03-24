def solution(id_list, report, k):
    # id_dict -> 딕셔너리, id_len -> 총 id 길이, id_list -> 리스트
    # report -> 신고 리스트, k -> 최대 옐로 카드 수
    # 행 -> 지가 신고한거, 열 -> 신고 당한거
    id_dict = dict()
    id_len = len(id_list)
    answer = [0] * id_len
    for i in range(len(id_list)):
        id_dict[id_list[i]] = i
    is_report = [[0] * id_len for _ in range(id_len)]
    for j in range(len(report)):
        reporter, reported = report[j].split()
        active = id_dict[reporter]
        passive = id_dict[reported]
        is_report[active][passive] = 1
    banned_list = []
    for c in range(id_len):
        cnt = 0
        for r in range(id_len):
            cnt += is_report[r][c]
            if k == cnt:
                banned_list.append(c)
                break
    for c in range(id_len):
        if c in banned_list:
            for r in range(id_len):
                if is_report[r][c]:
                    answer[r] += 1
    print(answer)
    return answer


solution(
    ["muzi", "frodo", "apeach", "neo"],
    ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],
    2
)