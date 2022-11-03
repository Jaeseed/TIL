from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    global MAP, cnt_of_cheeses
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    adj = [[0] * M for _ in range(N)]
    qu = deque()
    qu.append([0,0])
    while qu:
        r, c = qu.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr >= N or nr < 0 or nc >= M or nc < 0 or visited[nr][nc]: continue
            if MAP[nr][nc]:
                adj[nr][nc] += 1
            else:
                visited[nr][nc] = 1
                qu.append([nr,nc])
    for r in range(N):
        for c in range(M):
            if adj[r][c] > 1:
                MAP[r][c] = 0
                cnt_of_cheeses -= 1
    return


N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
cnt_of_cheeses = 0
hours = 0
for n in range(N):
    cnt_of_cheeses += sum(MAP[n])
while cnt_of_cheeses > 0:
    bfs()
    hours += 1
print(hours)