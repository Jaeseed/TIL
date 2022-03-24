def solution(lottos, win_nums):
    answer = []
    cnt = 0
    zero_cnt = 0
    for lotto in lottos:
        if lotto in win_nums:
            cnt += 1
        elif lotto == 0:
            zero_cnt += 1
    max_and_min = [cnt + zero_cnt, cnt]
    for i in max_and_min:
        if i >= 2:
            rank = 7 - i
        else:
            rank = 6
        answer.append(rank)
    return answer

solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19])