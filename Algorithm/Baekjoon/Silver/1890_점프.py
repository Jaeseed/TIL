N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
graph = [[0] * N for _ in range(N)]
graph[0][0] = 1
for r in range(N):
    for c in range(N):
        step = 1
        while True:
            nr = r - step
            if nr < 0: break
            if MAP[nr][c] == step:
                graph[r][c] += graph[nr][c]
            step += 1
        step = 1
        while True:
            nc = c - step
            if nc < 0: break
            if MAP[r][nc] == step:
                graph[r][c] += graph[r][nc]
            step += 1
print(graph[N-1][N-1])

