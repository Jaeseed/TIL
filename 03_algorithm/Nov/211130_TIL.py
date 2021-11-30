import sys

sys.stdin = open('input.txt', 'r')

# 백준 13460 구슬 탈출 2 #
from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]


def gravity(r, c, idx, another):
    nr = r + dr[idx]
    nc = c + dc[idx]
    while True:
        if MAP[nr][nc] == 'O':
            return nr, nc, 1
        if nr >= N or nr < 0 or nc >= M or nc < 0 or MAP[nr][nc] == '#' or (nr, nc) == another:
            nr -= dr[idx]
            nc -= dc[idx]
            return nr, nc, 0
        nr += dr[idx]
        nc += dc[idx]


N, M = map(int, input().split())

MAP = [list(input()) for _ in range(N)]

red = [0, 0]
blue = [0, 0]
for r in range(N):
    for c in range(M):
        if MAP[r][c] == 'R':
            MAP[r][c] = '.'
            red = [r, c]
        elif MAP[r][c] == 'B':
            MAP[r][c] = '.'
            blue = [r, c]
qu = deque()
qu.append((red[0], red[1], blue[0], blue[1], 0))
ans = 0
visited = [(red[0], red[1], blue[0], blue[1])]

while True:
    if ans != 0:
        break
    if len(qu) == 0:
        ans = -1
        break
    red_r, red_c, blue_r, blue_c, cnt = qu.popleft()
    if cnt == 10:
        ans = -1
        break
    for i in range(4):
        trr = red_r + dr[i]
        trc = red_c + dc[i]
        tbr = blue_r + dr[i]
        tbc = blue_c + dc[i]
        if trr >= N or trr < 0 or trc >= M or trc < 0 or MAP[trr][trc] == '#' or (trr, trc) == (blue_r, blue_c):
            if tbr >= N or tbr < 0 or tbc >= M or tbc < 0 or MAP[tbr][tbc] == '#':
                continue
        if (trr, trc) != (blue_r, blue_c):
            nrr, nrc, result_R = gravity(red_r, red_c, i, (-1, -1))
            nbr, nbc, result_B = gravity(blue_r, blue_c, i, (nrr, nrc))
        else:
            nbr, nbc, result_B = gravity(blue_r, blue_c, i, (-1, -1))
            nrr, nrc, result_R = gravity(red_r, red_c, i, (nbr, nbc))
        if result_B == 1:
            continue
        if result_R == 1:
            ans = cnt + 1
            break
        if (nrr,nrc,nbr,nbc) in visited:
            continue
        else:
            visited.append((nrr,nrc,nbr,nbc))
        qu.append((nrr, nrc, nbr, nbc, cnt + 1))
print(ans)