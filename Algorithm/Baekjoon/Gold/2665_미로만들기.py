from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    global graph
    qu = deque()
    qu.append([0, 0, 0])
    while qu:
        r, c, cnt = qu.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr >= N or nr < 0 or nc >= N or nc < 0: continue
            if MAP[nr][nc] == '1':
                if graph[nr][nc] <= cnt: continue
                qu.append([nr, nc, cnt])
                graph[nr][nc] = cnt
            else:
                if graph[nr][nc] <= cnt + 1: continue
                qu.append([nr,nc,cnt+1])
                graph[nr][nc] = cnt + 1
    return


N = int(input())
MAP = [list(input()) for _ in range(N)]
graph = [[2500] * N for _ in range(N)]
bfs()
print(graph[-1][-1])