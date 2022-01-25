import sys

dr = [1, 0, 0]
dc = [0, -1, 1]


def make_bridge(now_r, now_c, step):
    global MAP
    global min_try_cnt
    for c in range(now_c, N - 1):
        if c > now_c:
            now_r = 1
        for r in range(now_r, H + 1):
            if min_try_cnt <= step:
                return
            if MAP[r][c] == 0 and MAP[r][c + 1] == 0:
                MAP[r][c], MAP[r][c + 1] = 1, 2
                if ladder_game():
                    min_try_cnt = min(min_try_cnt, step)
                if step == 3:
                    MAP[r][c], MAP[r][c + 1] = 0, 0
                    continue
                make_bridge(r + 1, c, step+1)
                MAP[r][c], MAP[r][c + 1] = 0, 0


def ladder_game():
    for i in range(N):
        height = 0
        ni = i
        while True:
            height += 1
            if height == H+1:
                if ni != i:
                    return False
                break
            if MAP[height][ni] == 1:
                if ni + 1 < N and MAP[height][ni+1] == 2:
                    ni += 1
            elif MAP[height][ni] == 2:
                if ni - 1 >= 0 and MAP[height][ni-1] == 1:
                    ni -= 1

    return True


N, M, H = map(int, input().split())
MAP = [[0] * N for _ in range(H + 2)]
for m in range(M):
    a, b = map(int, sys.stdin.readline().split())
    MAP[a][b - 1], MAP[a][b] = 1, 2
min_try_cnt = 4
if ladder_game():
    min_try_cnt = 0
else:
    make_bridge(1, 0, 1)
if min_try_cnt == 4:
    min_try_cnt = -1
print(min_try_cnt)