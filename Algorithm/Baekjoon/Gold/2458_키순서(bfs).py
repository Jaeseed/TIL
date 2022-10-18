import sys
from collections import deque


def adjacency(start, direction):
    global go_visited, back_visited
    qu = deque()
    qu.append(start)
    while qu:
        now = qu.popleft()
        if direction == 1:
            for next_ in go[now]:
                if go_visited[start][next_]: continue
                go_visited[start][next_] = 1
                qu.append(next_)
        else:
            for next_ in back[now]:
                if back_visited[start][next_]: continue
                back_visited[start][next_] = 1
                qu.append(next_)
    return


N, M = map(int,input().split())
go = [[] for _ in range(N + 1)]
back = [[] for _ in range(N + 1)]
go_visited = [[0] * (N+1) for _ in range(N+1)]
back_visited = [[0] * (N+1) for _ in range(N+1)]
for m in range(M):
    short, tall = map(int, sys.stdin.readline().split())
    go[short].append(tall)
    back[tall].append(short)
for idx in range(1, N+1):
    adjacency(idx, 1)
    adjacency(idx, 2)
answer = 0
for i in range(1, N+1):
    if sum(go_visited[i]) + sum(back_visited[i]) == N - 1:
        answer += 1
print(answer)
