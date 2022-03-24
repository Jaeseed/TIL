gear_list = [0]
gear_list.append(list(map(int, input())))
gear_list.append(list(map(int, input())))
gear_list.append(list(map(int, input())))
gear_list.append(list(map(int, input())))
K = int(input())
for k in range(K):
    target, direction = map(int, input().split())
    rotate_list = [[target, direction]]
    idx = 0
    visited = [0] * 5
    visited[target] = 1
    while idx < len(rotate_list):
        now = rotate_list[idx][0]
        if now - 1 > 0 and visited[now - 1] == 0:
            if gear_list[now][-2] != gear_list[now - 1][2]:
                rotate_list.append([now - 1, rotate_list[idx][1] * (-1)])
                visited[now - 1] = 1
        if now + 1 <= 4 and visited[now + 1] == 0:
            if gear_list[now][2] != gear_list[now + 1][-2]:
                rotate_list.append([now + 1, rotate_list[idx][1] * (-1)])
                visited[now + 1] = 1
        idx += 1
    for tg, dc in rotate_list:
        if dc == -1:
            tmp = gear_list[tg][0]
            for i in range(7):
                gear_list[tg][i] = gear_list[tg][i + 1]
            gear_list[tg][-1] = tmp
        else:
            tmp = gear_list[tg][-1]
            for i in range(7, 0, -1):
                gear_list[tg][i] = gear_list[tg][i - 1]
            gear_list[tg][0] = tmp
ans = 0
for t in range(1, 5):
    if gear_list[t][0] == 1:
        ans += 2 ** (t - 1)
print(ans)
