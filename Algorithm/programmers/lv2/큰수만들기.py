def solution(number, k):
    answer = ''
    # 삭제된 개수
    delete_cnt = 0
    # idx의 삭제 유무
    delete_list = [0] * len(number)
    for idx in range(len(number)-1):
        # 역순으로 크기 비교할 idx
        back_idx = idx
        while back_idx >= 0 and delete_cnt < k:
            if int(number[back_idx]) >= int(number[idx + 1]):
                break
            if delete_list[back_idx] == 0:
                delete_cnt += 1
                delete_list[back_idx] = 1
            back_idx -= 1
    # 제거된 숫자 길이
    modified_cnt = len(number) - k
    now_cnt = 0
    for idx in range(len(number)):
        if delete_list[idx]: continue
        answer += number[idx]
        now_cnt += 1
        # 숫자 길이 충족 시 break
        if modified_cnt == now_cnt:
            break
    return answer
solution("1231234", 3)