from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r_, c_):
    global seconds
    visited = [[0] * N for _ in range(N)]
    visited[r_][c_] = 1
    fish_tong = []
    now_distance = 2e29
    qu = deque()
    qu.append([r_, c_, 0])
    flag = 0
    while flag == 0 and qu:
        r, c, cnt = qu.popleft()
        if cnt > now_distance:
            break
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr >= N or nr < 0 or nc >= N or nc < 0 or visited[nr][nc] == 1 or MAP[nr][nc] > shark_size: continue
            visited[nr][nc] = 1
            qu.append([nr, nc, cnt + 1])
            if 0 < MAP[nr][nc] < shark_size:
                if cnt <= now_distance:
                    now_distance = cnt
                    fish_tong.append([nr, nc])
    if now_distance == 2e29:
        return False
    else:
        seconds += cnt
        find_prey(fish_tong)
        return True


def find_prey(fish_tong):
    global shark_eat_cnt
    global shark_size
    global shark_r
    global shark_c
    min_r = N
    min_c = N
    for r, c in fish_tong:
        if r < min_r:
            min_r, min_c = r, c
        elif r == min_r:
            if c < min_c:
                min_c = c
    MAP[min_r][min_c] = 0
    shark_eat_cnt += 1
    shark_r, shark_c = min_r, min_c
    if shark_eat_cnt == shark_size:
        shark_eat_cnt = 0
        shark_size += 1
    return


N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
for row in range(N):
    for col in range(N):
        if MAP[row][col] == 9:
            shark_r, shark_c = row, col
            MAP[shark_r][shark_c] = 0
shark_size = 2
shark_eat_cnt = 0
seconds = 0
while True:
    if not bfs(shark_r, shark_c):
        break
print(seconds)
