import sys
from collections import deque

def bfs(t1,t2):
    qu = deque()
    qu.append([t1, 1])
    while qu:
        now, cnt = qu.popleft()
        for i in range(1,N+1):
            if MAP[now][i] == 1 and visited[now][i] > cnt:
                if i == t2:
                    return cnt
                qu.append([i,cnt+1])
                visited[now][i] = cnt
    return -1



N = int(input())
target1, target2 = map(int,input().split())
MAP = [[0] * (N+1) for _ in range(N+1)]
link_cnt = int(input())
for link in range(link_cnt):
    p1, p2 = map(int, sys.stdin.readline().split())
    MAP[p1][p2], MAP[p2][p1] = 1, 1
visited = [[2e29] * (N+1) for _ in range(N+1)]
ans = bfs(target1, target2)
print(ans)
