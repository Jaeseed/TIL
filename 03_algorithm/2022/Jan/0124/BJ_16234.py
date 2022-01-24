from collections import deque
dr = [-1,1,0,0]
dc = [0,0,-1,1]


def bfs(r, c, s):
    global MAP
    global population_list
    qu = deque()
    qu.append([r,c])
    total = MAP[r][c]
    cnt = 1
    while qu:
        r, c = qu.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr >= N or nr < 0 or nc >= N or nc < 0 or visited[nr][nc] != 0: continue
            if L <= abs(MAP[r][c] - MAP[nr][nc]) <= R:
                visited[nr][nc] = s
                total += MAP[nr][nc]
                cnt += 1
                qu.append([nr,nc])
    if cnt == 1:
        visited[r][c] = 0
        return False
    average = total // cnt
    population_list.append(average)
    return True


N, L, R = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
days = 0
while True:
    flag = 0
    visited = [[0] * N for _ in range(N)]
    step = 1
    population_list = [0]
    for row in range(N):
        for col in range(N):
            if visited[row][col] == 0:
                visited[row][col] = step
                if bfs(row, col, step):
                    flag = 1
                    step += 1
    if flag == 0:
        break
    for row in range(N):
        for col in range(N):
            if visited[row][col] > 0:
                MAP[row][col] = population_list[visited[row][col]]
    days += 1
print(days)