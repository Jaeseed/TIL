from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
square = [0, 1, 2, 3, 4, 5, 6]


def rolling(d):
    global square
    if d == 0:
        tmp = square[1]
        square[1] = square[4]
        square[4] = square[6]
        square[6] = square[3]
        square[3] = tmp
    elif d == 1:
        tmp = square[1]
        square[1] = square[2]
        square[2] = square[6]
        square[6] = square[5]
        square[5] = tmp
    elif d == 2:
        tmp = square[1]
        square[1] = square[3]
        square[3] = square[6]
        square[6] = square[4]
        square[4] = tmp
    elif d == 3:
        tmp = square[1]
        square[1] = square[5]
        square[5] = square[6]
        square[6] = square[2]
        square[2] = tmp

    return


def bfs(ro, co, target):
    visited = [[0] * M for _ in range(N)]
    visited[ro][co] = 1
    qu = deque()
    qu.append([ro, co])
    cnt = 1
    while qu:
        ro, co = qu.popleft()
        for i in range(4):
            nr_ = ro + dr[i]
            nc_ = co + dc[i]
            if nr_ >= N or nr_ < 0 or nc_ >= M or nc_ < 0 or visited[nr_][nc_] or MAP[nr_][nc_] != target: continue
            qu.append([nr_, nc_])
            visited[nr_][nc_] = 1
            cnt += 1
    return cnt


N, M, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
trials = 0
ans = 0
direction = 0
r, c = 0, 0
while trials < K:
    nr = r + dr[direction]
    nc = c + dc[direction]
    if nr >= N or nr < 0 or nc >= M or nc < 0:
        direction = (direction + 2) % 4
        nr = r + dr[direction]
        nc = c + dc[direction]
    r, c = nr, nc
    rolling(direction)
    if square[6] > MAP[r][c]:
        direction = (direction + 1) % 4
    elif square[6] < MAP[r][c]:
        direction = (direction - 1) % 4
    ret = bfs(r, c, MAP[r][c])
    ans += ret * MAP[r][c]
    trials += 1
print(ans)