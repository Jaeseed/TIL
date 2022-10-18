import sys
N, M = map(int,input().split())
INF = 2e29
adj = [[INF] * N for _ in range(N)]
for n in range(N):
    adj[n][n] = 0
for m in range(M):
    short, tall = map(int,sys.stdin.readline().split())
    adj[short-1][tall-1] = 1
    adj[tall-1][short-1] = -1
for s in range(N):
    for e in range(N):
        if adj[s][e] != INF:
            continue
        for mid in range(N):
            if adj[s][mid] == adj[mid][e] and adj[mid][e] != INF:
                adj[s][e] = adj[s][mid]
                adj[e][s] = -adj[s][mid]
                break
answer = 0
for i in range(N):
    flag = 1
    for j in range(N):
        if adj[i][j] == INF:
            flag = 0
            break
    if flag == 1:
        answer += 1

print(answer)