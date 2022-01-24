from collections import deque
dr = [-1,1,0,0]
dc = [0,0,-1,1]


def bfs(r, c):
    global MAP
    used = [[0] * N for _ in range(N)]
    used[r][c] = 1
    qu = deque()
    qu.append([r,c])
    total = MAP[r][c]
    cnt = 1
    while qu:
        r, c = qu.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr >= N or nr < 0 or nc >= N or nc < 0 or visited[nr][nc] == 1: continue
            if L <= abs(MAP[r][c] - MAP[nr][nc]) <= R:
                used[nr][nc], visited[nr][nc] = 1, 1
                total += MAP[nr][nc]
                cnt += 1
                qu.append([nr,nc])
    if cnt == 1:
        return False
    average = total // cnt
    for r in range(N):
        for c in range(N):
            if used[r][c] == 1:
                MAP[r][c] = average
    return True


N, L, R = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
days = 0
while True:
    flag = 0
    visited = [[0] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if visited[row][col] == 0:
                visited[row][col] = 1
                if bfs(row, col):
                    flag = 1
    if flag == 0:
        break
    days += 1
print(days)
