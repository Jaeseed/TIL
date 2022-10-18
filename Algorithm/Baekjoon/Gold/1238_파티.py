import sys
from heapq import heappop, heappush


def search(s):
    heap = []
    heappush(heap, [0, s])
    clear = [0] * (N+1)
    while heap:
        now_t, now = heappop(heap)
        if clear[now]:
            continue
        clear[now] = 1
        graph[s][now] = now_t
        for next_, t in node[now]:
            if graph[now][next_]:
                if clear[next_]:
                    continue
                heappush(heap, [now_t + graph[now][next_], next_])
            else:
                heappush(heap, [now_t + t, next_])


N, M, X = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]
node = [[] for _ in range(N + 1)]
for m in range(M):
    start, end, time = map(int, sys.stdin.readline().split())
    node[start].append([end, time])
for n in range(1, N + 1):
    search(n)
answer = 0
for n in range(1, N+1):
    answer = max(answer, graph[n][X] + graph[X][n])
print(answer)