from collections import deque
dr = [-1,1,0,0]
dc = [0,0,-1,1]


def bfs(ro,co):
    global visited
    cnt = 1
    qu = deque()
    qu.append([ro,co])
    while qu:
        r, c = qu.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr >= N or nr < 0 or nc >= M or nc < 0 or visited[nr][nc] or MAP[nr][nc]: continue
            cnt += 1
            qu.append([nr,nc])
            visited[nr][nc] = 1
    return cnt


N, M, K = map(int,input().split())
MAP = [[0] * (M+1) for _ in range(N+1)]
# 1. 2차원 배열 누적합 적용
# 1-1. 네 꼭지점에 각 부여
for k in range(K):
    c1, r1, c2, r2 = map(int,input().split())
    MAP[r1][c1] += 1
    MAP[r1][c2] -= 1
    MAP[r2][c1] -= 1
    MAP[r2][c2] += 1

# 1-2. 누적합 구하기
for n in range(N):
    for m in range(M-1):
        MAP[n][m+1] += MAP[n][m]
for m in range(M):
    for n in range(N-1):
        MAP[n+1][m] += MAP[n][m]

# 방문 확인
visited = [[0] * M for _ in range(M)]
answer = []

# 2. bfs로 구역 수  구하기
for n in range(N):
    for m in range(M):
        if visited[n][m] == 0 and MAP[n][m] == 0:
            visited[n][m] = 1
            answer.append(bfs(n,m))

print(len(answer))
print(*sorted(answer))
