import sys
N = int(input())
M = int(input())
INF = 2e29
adj = [[INF] * N for _ in range(N)]
for m in range(M):
    st, en, ti = map(int,sys.stdin.readline().split())
    adj[st-1][en-1] = min(adj[st-1][en-1], ti)
for n in range(N):
    adj[n][n] = 0
for m in range(N):
    for i in range(N):
        for j in range(N):
            adj[i][j] = min(adj[i][j], adj[i][m] + adj[m][j])
for i in range(N):
    for j in range(N):
        if adj[i][j] == INF:
            adj[i][j] = 0
for n in range(N):
    print(' '.join(map(str, adj[n])))