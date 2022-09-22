import sys
from heapq import heappop, heappush


def search(s,e):
    heap = []
    heappush(heap, [0,s])
    while heap:
        t, now = heappop(heap)
        for i in range(len(MAP[now])):
            next_ = MAP[now][i]
            if next_[0] == X:
                return t + next_[1]
            heappush(heap, [t + next_[1], next_[0]])
    return


N, M, X = map(int,input().split())
MAP = [[] for _ in range(N+1)]
for m in range(M):
    start, end, time = map(int,sys.stdin.readline().split())
    MAP[start].append([end,time])
for n in range(1, N+1):
    MAP[n].sort(key=lambda x:x[1])
answer = 0
for n in range(1, N+1):
    if n == X: continue
    go = search(n,X)
    come = search(X,n)
    answer = max(answer, go+come)
print(answer)