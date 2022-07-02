N = int(input())
graph = [[0] * 10 for _ in range(N)]
for i in range(1, 10):
    graph[0][i] = 1

for n in range(1, N):
    for m in range(10):
        high_idx = m + 1
        low_idx = m - 1
        high_value = 0
        low_value = 0
        if 0 <= high_idx < 10:
            high_value = graph[n-1][high_idx]
        if 0 <= low_idx < 10:
            low_value = graph[n-1][low_idx]
        graph[n][m] = high_value + low_value
answer = sum(graph[N-1])
print(answer % 1000000000)