from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    global visited
    cnt = 1
    qu = deque()
    qu.append([r, c])
    while qu:
        r, c = qu.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr >= N or nr < 0 or nc >= N or nc < 0 or visited[nr][nc] == 1 or MAP[nr][nc] == '0': continue
            visited[nr][nc] = 1
            qu.append([nr, nc])
            cnt += 1
    return cnt


N = int(input())
MAP = [input() for _ in range(N)]
visited = [[0] * N for _ in range(N)]
apartment_list = []
for row in range(N):
    for col in range(N):
        if MAP[row][col] == '1' and visited[row][col] == 0:
            visited[row][col] = 1
            ret = bfs(row, col)
            apartment_list.append(ret)
apartment_list.sort()
print(len(apartment_list))
for idx in range(len(apartment_list)):
    print(apartment_list[idx])
