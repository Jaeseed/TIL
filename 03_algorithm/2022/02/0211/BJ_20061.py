import sys


def move_block():
    global spot_g, spot_b, green, blue
    row_g, col_b = 6, 6
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
        row_g = min(row_g, r + plus - 1)

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
        blue[r][c+ plus-1] = 1
        col_b = min(col_b, c + plus - 1)

    return row_g, col_b


def ans_plus():
    global scores
    deleted = [0,0,0,0]
    for r in range(6):
        cnt = 0
        for c in range(4):
            if green[r][c]:
                cnt += 1
        if cnt == 4:
            deleted[0] += 1
            deleted[1] = r
            scores += 1
            for c in range(4):
                green[r][c] = 0

    for c in range(6):
        cnt = 0
        for r in range(4):
            if blue[r][c]:
                cnt += 1
        if cnt == 6:
            deleted[2] += 1
            deleted[3] = c
            scores += 1
            for r in range(4):
                blue[r][c] = 0

    return deleted


def gravity(deleted):
    global green, blue
    total_cnt_g, end_g, total_cnt_b, end_b = deleted
    distance_g = total_cnt_g
    distance_b = total_cnt_b
    while total_cnt_g:
        for c in range(4):
            green[end_g][c] = green[end_g - distance_g][c]
            green[end_g][c] = 0
        total_cnt_g -= 1
    while total_cnt_b:
        for r in range(4):
            blue[r][end_b] = blue[r][end_b - distance_b]
            blue[r][end_b] = 0
        total_cnt_b -= 1
    return


def slicing(g, b):
    global green, blue
    slice_g = 2 - g
    slice_b = 2 - b
    if g < 2:
        for c in range(4):
            for i in range(1, slice_g+1):
                green[-i][c] = 0
        for c in range(4):
            for r in range(5, 3 - slice_g, -1):
                green[r][c] = green[r - 1][c]
                green[r][c - 1] = 0
    if b < 2:
        for r in range(4):
            for i in range(1, slice_b+1):
                blue[r][-i] = 0
        for r in range(4):
            for c in range(5, 3 - slice_b, -1):
                blue[r][c] = blue[r][c-1]
                blue[r][c-1] = 0
    return


N = int(input())
green = [[0] * 4 for _ in range(6)]
blue = [[0] * 6 for _ in range(4)]
scores = 0
for n in range(N):
    t, r_, c_ = map(int, sys.stdin.readline().split())
    if t == 1:
        spot_g = [[0,c_]]
        spot_b = [[r_,0]]
    elif t == 3:
        spot_g = [[0,c_],[1,c_]]
        spot_b = [[r_,0],[r_+1,0]]
    else:
        spot_g = [[0, c_], [0, c_ + 1]]
        spot_b = [[r_,0],[r_,1]]
    value_g, value_b = move_block()
    ret = ans_plus()
    if ret[0] or ret[2]:
        gravity(ret)
    if value_g <= 1 or value_b <= 1:
        slicing(value_g,value_b)
total_cnt = 0
for s in range(6):
    for d in range(4):
        total_cnt += green[s][d] + blue[d][s]

print(scores)
print(total_cnt)
