from collections import deque
import sys


def bfs(x):
    global answer
    qu = deque()
    qu.append([x,0])
    visited = [0] * (N+1)
    visited[x] = 1
    while qu:
        now, cnt = qu.popleft()
        for next_ in graph[now]:
            if visited[next_]: continue
            visited[next_] = 1
            if cnt + 1 == K:
                answer.append(next_)
            else:
                qu.append([next_, cnt + 1])
    return


N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for m in range(M):
    s, e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
answer = []
bfs(X)
answer.sort()
if answer:
    for a in answer:
        print(a)
else:
    print(-1)