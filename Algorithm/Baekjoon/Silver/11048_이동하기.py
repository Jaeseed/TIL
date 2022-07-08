N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
graph = [[0] * M for _ in range(N)]
graph[0][0] = MAP[0][0]
for n in range(1, N):
    graph[n][0] = graph[n-1][0] + MAP[n][0]
for m in range(1, M):
    graph[0][m] = graph[0][m-1] + MAP[0][m]
for n in range(1, N):
    for m in range(1, M):
        tmp = max(graph[n-1][m], graph[n][m-1])
        graph[n][m] = tmp + MAP[n][m]
print(graph[N-1][M-1])
