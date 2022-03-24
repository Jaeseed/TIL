import sys


def dfs(now):
    global visited
    visited[now] = 1
    for j in range(1, N+1):
        if MAP[now][j] == 1 and visited[j] == 0:
            dfs(j)
    return


N = int(input())
link = int(input())
MAP = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(link):
    com1, com2 = map(int, sys.stdin.readline().split())
    MAP[com1][com2] = 1
    MAP[com2][com1] = 1
visited = [0] * (N + 1)
visited[1] = 1
dfs(1)
print(sum(visited) - 1)
