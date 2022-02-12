import sys


def move_block():
    global spot_g, spot_b, green, blue
    flag_g = 1
    flag_b = 1
    # green move down
    plus = 0
    while flag_g:
        plus += 1
        for i in range(len(spot_g)):
            r = spot_g[i][0]
            c = spot_g[i][1]
            if r + plus >= 6 or green[r + plus][c]:
                flag_g = 0
    for i in range(len(spot_b)):
        r = spot_g[i][0]
        c = spot_g[i][1]
        green[r + plus - 1][c] = 1

    # blue move down
    plus = 0
    while flag_b:
        plus += 1
        for i in range(len(spot_g)):
            r = spot_b[i][0]
            c = spot_b[i][1]
            if c + plus >= 6 or blue[r][c + plus]:
                flag_b = 0
    for i in range(len(spot_b)):
        r = spot_b[i][0]
        c = spot_b[i][1]
        blue[r][c + plus - 1] = 1

    return


def ans_plus():
    global scores, green, blue
    deleted = [0, 0, 0, 0]
    for r in range(2, 6):
        cnt = 0
        for c in range(4):
            if green[r][c]:
                cnt += 1
        if cnt == 4:
            deleted[0] += 1
            deleted[1] = r
            scores += 1

    for c in range(2, 6):
        cnt = 0
        for r in range(4):
            if blue[r][c]:
                cnt += 1
        if cnt == 4:
            deleted[2] += 1
            deleted[3] = c
            scores += 1
    return deleted


def gravity(deleted):
    global green, blue
    distance_g, end_g, distance_b, end_b = deleted
    if end_g != 0:
        for r in range(end_g, distance_g-1, -1):
            for c in range(4):
                green[r][c] = green[r - distance_g][c]
                green[r - distance_g][c] = 0
    if end_b != 0:
        for c in range(end_b, distance_b-1, -1):
            for r in range(4):
                blue[r][c] = blue[r][c - distance_b]
                blue[r][c - distance_b] = 0
    return


def slicing():
    global green, blue
    tmp_g, tmp_b = 10, 10
    for i in range(4):
        for j in range(2):
            if green[j][i]:
                tmp_g = min(tmp_g, j)
            if blue[i][j]:
                tmp_b = min(tmp_b, j)
    slice_g = 2 - tmp_g
    slice_b = 2 - tmp_b
    if tmp_g < 2:
        for r in range(5, 1, -1):
            for c in range(4):
                green[r][c] = green[r - slice_g][c]
                green[r - slice_g][c] = 0
    if tmp_b < 2:
        for c in range(5, 1, -1):
            for r in range(4):
                blue[r][c] = blue[r][c - slice_b]
                blue[r][c - slice_b] = 0
    return


N = int(input())
green = [[0] * 4 for _ in range(6)]
blue = [[0] * 6 for _ in range(4)]
scores = 0
for n in range(N):
    t, r_, c_ = map(int, sys.stdin.readline().split())
    if t == 1:
        spot_g = [[0, c_]]
        spot_b = [[r_, 0]]
    elif t == 2:
        spot_g = [[0, c_], [0, c_ + 1]]
        spot_b = [[r_, 0], [r_, 1]]
    else:
        spot_g = [[0, c_], [1, c_]]
        spot_b = [[r_, 0], [r_ + 1, 0]]
    move_block()
    ret = ans_plus()
    if ret[0] or ret[2]:
        gravity(ret)
    slicing()
total_cnt = 0
for s in range(6):
    for d in range(4):
        total_cnt += green[s][d] + blue[d][s]

print(scores)
print(total_cnt)