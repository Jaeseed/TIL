from collections import deque


def bfs(row, col):
    global visited
    qu = deque()
    qu.append([row,col,0])
    while qu:
        r, c, cnt = qu.popleft()
        for i in range(N):
            nr = r + dr[i]
            nc = c + dc[i]
            # 리스트를 벗어나거나, 가로 블록일 때 제외
            if nr >= R or nr < 1 or nc >= C or nc < 1 or MAP[nr][nc] == 0: continue
            # 방문 체크
            if visited[nr][nc] != 0 and visited[nr][nc] <= cnt + 1: continue
            if nr == R - 1:
                return cnt + 1
            qu.append([nr,nc,cnt+1])
            visited[nr][nc] = cnt + 1
    return -1


R, C = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(R)]
dr = []
dc = []
N = int(input())
for n in range(N):
    dr_n, dc_n = map(int, input().split())
    dr.append(dr_n)
    dc.append(dc_n)
answer = -1
visited = [[0] * C for _ in range(R)]
for k in range(C):
    if MAP[0][k] == 0:
        continue
    ret = bfs(0, k)
    if ret != -1:
        if answer == -1:
            answer = ret
        else:
            answer = min(ret, answer)
print(answer)
