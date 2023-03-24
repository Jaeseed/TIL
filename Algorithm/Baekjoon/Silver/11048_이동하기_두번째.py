from collections import deque
dr = [1, 0]
dc = [0, 1]


def bfs():
    global visited, graph
    qu = deque()
    qu.append([0,0])
    while qu:
        r, c = qu.popleft()
        for i in range(2):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr >= N or nc >= M or graph[nr][nc] >= graph[r][c] + MAP[nr][nc] > 0: continue
            graph[nr][nc] = graph[r][c] + MAP[nr][nc]
            if visited[nr][nc] == 0:
                visited[nr][nc] = 1
                qu.append([nr,nc])
    return


N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
graph = [[0] * M for _ in range(N)]
graph[0][0] = MAP[0][0]
visited= [[0] * M for _ in range(N)]
bfs()
print(graph[N-1][M-1])
