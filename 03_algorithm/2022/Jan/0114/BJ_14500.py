dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c, value, step, test):
    global max_value
    global visited
    if step == 4:
        max_value = max(max_value, value)
        return
    if value + max_spot * (4-step) < max_value:
        return
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr >= N or nr < 0 or nc >= M or nc < 0 or visited[nr][nc] == 1: continue
        visited[nr][nc] = 1
        if step == 2:
            dfs(r,c,value+MAP[nr][nc],step+1,test+str(r)+str(c))
        dfs(nr,nc,value+MAP[nr][nc], step+1,test+str(nr)+str(nc))
        visited[nr][nc] = 0


N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
max_spot = 0
for row in range(N):
    for col in range(M):
        max_spot = max(MAP[row][col], max_spot)
max_value = 0
visited = [[0] * M for _ in range(N)]
for row in range(N):
    for col in range(M):
        visited[row][col] = 1
        dfs(row, col, MAP[row][col], 1,str(row)+str(col))
        visited[row][col] = 0

print(max_value)
