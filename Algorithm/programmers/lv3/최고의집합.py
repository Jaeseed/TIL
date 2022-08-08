def solution(n, s):
    if n > s:
        return [-1]
    mean = s // n
    remainder = s % n
    answer = [mean] * n
    uncleared_cnt = n - 1
    while uncleared_cnt > 0:
        new_mean = remainder // uncleared_cnt
        new_remainder = remainder % uncleared_cnt
        if new_mean == 0:
            uncleared_cnt -= 1
            continue
        for i in range(n-1, n - 1 - uncleared_cnt, -1):
            answer[i] += new_mean
        remainder = new_remainder
    return answer