from collections import deque


def bfs():
    global N
    qu = deque()
    qu.append([N, 0])
    if N > K:
        visited = [0] * (N+1)
    else:
        visited = [0] * (K * 2)
    visited[N] = 1
    while qu:
        now, cnt = qu.popleft()
        # 1. -1
        if now - 1 == K or now + 1 == K or now * 2 == K:
            return cnt + 1
        if now > 0 and visited[now-1] == 0:
            qu.append([now-1, cnt + 1])
            visited[now-1] = 1
        # 2. +1
        if now < K and visited[now+1] == 0:
            qu.append([now+1, cnt + 1])
            visited[now+1] = 1
        # 3. *2
        if now < K and visited[now*2] == 0:
            qu.append([now*2, cnt+1])
            visited[now+1] = 1


N, K = map(int, input().split())
if N == K:
    print(0)
else:
    print(bfs())
