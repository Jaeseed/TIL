import sys
from collections import deque


def bfs():
    global visited_cnt, answer
    qu = deque()
    qu.append(1)
    while visited_cnt < N:
        now = qu.popleft()
        for i in tree[now]:
            if answer[i] != 0:
                continue
            answer[i] = now
            visited_cnt += 1
            qu.append(i)
    return


N = int(input())
tree = [[] for _ in range(N + 1)]
for n in range(N - 1):
    n1, n2 = map(int, sys.stdin.readline().split())
    tree[n1].append(n2)
    tree[n2].append(n1)
visited_cnt = 1
answer = [0] * (N + 1)
answer[1] = -1
bfs()
for a in range(2, N + 1):
    print(answer[a])
