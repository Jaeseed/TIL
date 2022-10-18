N = int(input())
adj = [list(map(int,input().split())) for _ in range(N)]
floyd = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if adj[i][j]:
            floyd[i][j] = 1
for n in range(N):
    for i in range(N):
        for j in range(N):
            if floyd[i][n] == floyd[n][j] == 1:
                floyd[i][j] = 1
for n in range(N):
    print(' '.join(map(str,floyd[n])))