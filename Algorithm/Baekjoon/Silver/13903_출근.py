from collections import deque


def bfs():
    qu = deque()
    for c2 in range(C):
        if MAP[0][c2] == 1:
            qu.append([0,c2,0])
    visited = [[0] * C for _ in range(R)]
    while qu:
        r, c, cnt = qu.popleft()
        if visited[r][c] != cnt: continue
        for i in range(N):
            nr = r + dr[i]
            nc = c + dc[i]
            # 리스트를 벗어나거나, 가로 블록일 때 제외
            if nr >= R or nr < 1 or nc >= C or nc < 0 or MAP[nr][nc] == 0: continue
            # 방문 체크
            if 0 < visited[nr][nc] <= cnt + 1: continue
            if nr == R - 1:
                return cnt + 1
            qu.append([nr,nc,cnt+1])
            visited[nr][nc] = cnt + 1
    return -1


R, C = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(R)]
if R == 1:
    answer = -1
    for c1 in range(C):
        if MAP[0][c1] == 1:
            answer = 0
    print(answer)
else:
    dr = []
    dc = []
    N = int(input())
    for n in range(N):
        dr_n, dc_n = map(int, input().split())
        dr.append(dr_n)
        dc.append(dc_n)
    print(bfs())

