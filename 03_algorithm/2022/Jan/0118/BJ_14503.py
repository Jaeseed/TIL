dr = [-1,0,1,0]
dc = [0,1,0,-1]


def clean(row, col, d):
    global cnt
    for i in range(1,5):
        now_d = (d + 4 - i) % 4
        nr = row + dr[now_d]
        nc = col + dc[now_d]
        if nr >= N or nr < 0 or nc >= M or nc < 0 or MAP[nr][nc] != 0: continue
        MAP[nr][nc] = -1
        cnt += 1
        return nr, nc, now_d
    tmp_d = (now_d+2) % 4
    nr, nc = r + dr[tmp_d], c + dc[tmp_d]
    if nr >= N or nr < 0 or nc >= M or nc < 0 or MAP[nr][nc] == 1:
        return -1, -1, -1
    else:
        return nr, nc, now_d


N, M = map(int,input().split())
r, c, direction = map(int,input().split())
MAP = [list(map(int,input().split())) for _ in range(N)]
MAP[r][c] = -1
cnt = 1

while True:
    r, c, direction = clean(r, c, direction)
    if r == -1:
        break
print(cnt)
