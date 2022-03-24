dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]


def diffusion(r_, c_, d):
    global MAP, ans
    yr = r_ + dr[d]
    yc = c_ + dc[d]
    yyr, yyc = yr + dr[d], yc + dc[d]
    remain_sand = MAP[yr][yc]
    left = (d - 1) % 4
    right = (d + 1) % 4
    drl, dcl, drr, dcr, drd, dcd = dr[left], dc[left], dr[right], dc[right], dr[d], dc[d]
    # 좌측
    tong = [
        [drl, dcl, 0.01],
        [drl + drd, dcl + dcd, 0.07],
        [drl * 2 + drd, dcl * 2 + dcd, 0.02],
        [drl + drd * 2, dcl + dcd * 2, 0.1],
        [drr, dcr, 0.01],
        [drr + drd, dcr + dcd, 0.07],
        [drr * 2 + drd, dcr * 2 + dcd, 0.02],
        [drr + drd * 2, dcr + dcd * 2, 0.1],
        [drd * 3, dcd * 3, 0.05]
    ]
    for i in range(9):
        pr, pc, percent = tong[i][0], tong[i][1], tong[i][2]
        value = int(MAP[yr][yc] * percent)
        if r_ + pr >= N or r_ + pr < 0 or c_ + pc >= N or c_ + pc < 0:
            ans += value
        else:
            MAP[r_ + pr][c_ + pc] += value
        remain_sand -= value
    MAP[yr][yc] = 0
    if yyr >= N or yyr < 0 or yyc >= N or yyc < 0:
        ans += remain_sand
    else:
        MAP[yyr][yyc] += remain_sand
    return yr, yc


N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
ans = 0
r = c = N // 2
idx = 0
while r != 0 or c != 0:
    visited[r][c] = 1
    if r == c == N // 2:
        pass
    else:
        tmp = (idx + 1) % 4
        if visited[r + dr[tmp]][c + dc[tmp]] == 0:
            idx = tmp
    r, c = diffusion(r, c, idx)
print(ans)