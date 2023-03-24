from collections import deque

s, t = map(int, input().split())
if s == t:
    print(0)
elif t == 0:
    print('-')
elif t == 1:
    print('/')
else:
    qu = deque()
    qu += [[s * 2, 1, '+'], [1, 1, '/'], [s * s, 1, '*']]
    flag = 0
    answer_list = []
    while qu:
        now, cnt, order = qu.popleft()
        if flag == 1 and len(answer_list[0]) != cnt:
            break
        if now == t:
            answer_list.append(order)
            flag = 1
        sqrt = now * now
        double = 2 * now
        if sqrt <= t and sqrt != 1:
            qu.append([sqrt, cnt + 1, order + '*'])
        if double <= t:
            qu.append([double, cnt + 1, order + '+'])
    if answer_list:
        answer_list.sort()
        print(answer_list[0])
    else:
        print(-1)
