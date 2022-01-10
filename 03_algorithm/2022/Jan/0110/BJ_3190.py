from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def move(goal_sec, idx):
    global MAP
    global now_sec, snake_body
    while now_sec != goal_sec:
        r, c = snake_body[-1][0], snake_body[-1][1]
        hr = r + dr[idx]
        hc = c + dc[idx]
        if hr >= N or hr < 0 or hc >= N or hc < 0 or MAP[hr][hc] == 1:
            now_sec += 1
            return True
        snake_body.append([hr, hc])
        if MAP[hr][hc] != 2:
            tr, tc = snake_body.popleft()
            MAP[tr][tc] = 0
        MAP[hr][hc] = 1
        now_sec += 1
    return False


N = int(input())
K = int(input())
MAP = [[0] * N for _ in range(N)]
for k in range(K):
    row, col = map(int, input().split())
    row -= 1
    col -= 1
    MAP[row][col] = 2
L = int(input())
direction_idx = 0
now_sec = 0
snake_body = deque()
snake_body.append([0, 0])
MAP[0][0] = 1
flag = 0
for _ in range(L):
    X, C = input().split()
    if move(int(X), direction_idx):
        flag = 1
        break
    if C == 'D':
        direction_idx += 1
        direction_idx %= 4
    else:
        if direction_idx > 0:
            direction_idx -= 1
        else:
            direction_idx += 3
if flag == 0:
    move(2e29, direction_idx)
print(now_sec)
