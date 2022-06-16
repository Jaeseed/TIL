import sys


def calculate(list_):
    global all_cnt
    now = all_cases
    for case in cnt_list:
        for unit in range(2, case + 1):
            now //= unit
    all_cnt += now
    return


T = int(input())
answer = ''
for t in range(T):
    n, m = map(int, sys.stdin.readline().split())
    dif = m * 3 - n
    if dif < 0:
        answer += str(0) + '\n'
        continue
    cnt_list = [dif // 2, dif % 2, 0]
    cnt_list[2] = m - cnt_list[0] - cnt_list[1]
    all_cnt = 0
    all_cases = 1
    for m_ in range(1, m + 1):
        all_cases *= m_
    calculate(cnt_list)
    while cnt_list[0] > 0 and cnt_list[2] > 0:
        cnt_list[0] -= 1
        cnt_list[1] += 2
        cnt_list[2] -= 1
        calculate(cnt_list)
    answer += str(all_cnt % 1000000009) + '\n'
answer = answer[:-1]
print(answer)
