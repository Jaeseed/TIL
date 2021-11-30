import sys

sys.stdin = open('input.txt', 'r')

# 백준 13460 구슬 탈출 2 #
from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]


def gravity(nr, nc, idx):
    while True:
        nr += dr[idx]
        nc += dc[idx]
        if MAP[nr][nc] == 'O':
            return nr, nc, 1
        if MAP[nr][nc] == '#':
            nr -= dr[idx]
            nc -= dc[idx]
            return nr, nc, 0


N, M = map(int, input().split())

MAP = [list(input()) for _ in range(N)]

for r in range(N):
    for c in range(M):
        if MAP[r][c] == 'R':
            red = [r, c]
        elif MAP[r][c] == 'B':
            blue = [r, c]
qu = deque()
qu.append((red[0], red[1], blue[0], blue[1], 0))
ans = -1
visited = [(red[0], red[1], blue[0], blue[1])]

while qu:
    if ans != -1:
        break
    red_r, red_c, blue_r, blue_c, cnt = qu.popleft()
    if cnt == 10:
        ans = -1
        break
    for i in range(4):
        nrr, nrc, result_R = gravity(red_r, red_c, i)
        nbr, nbc, result_B = gravity(blue_r, blue_c, i)
        if nrr == nbr and nrc == nbc:
            if abs(nrr-red_r) + abs(nrc-red_c) > abs(nbr-blue_r) + abs(nbc-blue_c):
                nrr -= dr[i]
                nrc -= dc[i]
            else:
                nbr -= dr[i]
                nbc -= dc[i]
        if result_B == 1:
            continue
        if result_R == 1:
            ans = cnt + 1
            break
        if (nrr, nrc, nbr, nbc) in visited:
            continue
        visited.append((nrr, nrc, nbr, nbc))
        qu.append((nrr, nrc, nbr, nbc, cnt + 1))
print(ans)
