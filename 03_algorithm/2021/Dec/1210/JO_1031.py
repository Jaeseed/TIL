def remove(target):
    for n in range(5):
        for m in range(5):
            if MAP[n][m] == target:
                MAP[n][m] = 0
                return


def bingo():
    global bingo_cnt
    # 가로
    for n in range(5):
        if MAP[n][0] == 0:
            tmp = 1
            for m in range(1, 5):
                if MAP[n][m] == 0:
                    tmp += 1
                else:
                    break
            if tmp == 5:
                bingo_cnt += 1
        if bingo_cnt == 3:
            return
    # 세로
    for m in range(5):
        if MAP[0][m] == 0:
            tmp = 1
            for n in range(1, 5):
                if MAP[n][m] == 0:
                    tmp += 1
                else:
                    break
            if tmp == 5:
                bingo_cnt += 1
        if bingo_cnt == 3:
            return
    tmp_flag = 1
    for i in range(5):
        if MAP[i][i] > 0:
            tmp_flag = 0
    if tmp_flag == 1:
        bingo_cnt += 1
    tmp_flag = 1
    for j in range(5):
        if MAP[4-j][j] > 0:
            tmp_flag = 0
    if tmp_flag == 1:
        bingo_cnt += 1
    return


MAP = [list(map(int,input().split())) for _ in range(5)]
order_list = [list(map(int,input().split())) for _ in range(5)]
cnt = 0
ans_cnt = 0
flag = 0
for r in range(5):
    if flag == 1:
        break
    for c in range(5):
        ans_cnt += 1
        order = order_list[r][c]
        remove(order)
        cnt += 1
        if cnt > 4:
            bingo_cnt = 0
            bingo()
            if bingo_cnt > 2:
                flag = 1
                break

print(ans_cnt)

