import sys

sys.stdin = open('input.txt', 'r')

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

check_dr = [1, 0]
check_dc = [0, 1]


def find_min():
    min_value = min(fishbowls)
    for m in range(N):
        if fishbowls[m] == min_value:
            fishbowls[m] += 1
    return


def stack():
    width = 1
    height = 1
    turn = 0
    is_square = 1
    while width * height <= N:
        if turn % 2:
            width += 1
        else:
            height += 1
        turn += 1
    if width == height:
        width -= 1
        is_square = 0
    else:
        height -= 1
    area = width * height
    stump = N - area
    cnt = 0

    for i in range(N - 1, N - 1 - stump - width, -1):
        MAP[-1][i] = fishbowls[-1 - cnt]
        cnt += 1

    r = N - 1
    c = N - stump - width
    height -= 1
    area_cnt = 0
    direction_cnt = 0
    fish_idx = 1
    idx = 0
    length = [height, width]
    length_idx = 0
    nr, nc = r, c
    while area_cnt < area-width:
        nr += dr[idx]
        nc += dc[idx]
        MAP[nr][nc] = fishbowls[c - fish_idx]
        fish_idx += 1
        area_cnt += 1
        direction_cnt += 1
        if direction_cnt == length[length_idx]:
            idx += 1
            length_idx += 1
            idx, length_idx = idx % 4, length_idx % 2
            length[length_idx] -= 1
            direction_cnt = 0
    return


def fish_move():
    move_tong = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if MAP[r][c] > 0:
                for i in range(2):
                    nr = r + check_dr[i]
                    nc = c + check_dc[i]
                    if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
                    if MAP[nr][nc] == 0: continue
                    tmp = abs(MAP[nr][nc] - MAP[r][c]) // 5
                    if MAP[nr][nc] < MAP[r][c]:
                        tmp = -tmp
                    move_tong[r][c] += tmp
                    move_tong[nr][nc] -= tmp
    for row in range(N):
        for col in range(N):
            MAP[row][col] += move_tong[row][col]
    return


def make_arr():
    idx = 0
    for c in range(N):
        for r in range(N - 1, -1, -1):
            if MAP[r][c] == 0:
                break
            fishbowls[idx] = MAP[r][c]
            idx += 1
    return


def fold():
    for c in range(N):
        MAP[-1][c] = fishbowls[c]
    idx = 0
    for c in range(N//2-1, -1, -1):
        MAP[-2][N//2+idx] = MAP[-1][c]
        MAP[-1][c] = 0
        idx += 1
    idx = 0
    r_idx = 0
    for r in range(N-2,N):
        for c in range((N//4*3)-1,N//2-1,-1):
            MAP[N-3-r_idx][N//4*3+idx] = MAP[r][c]
            MAP[r][c] = 0
            idx += 1
        idx = 0
        r_idx = 1
    return


N, K = map(int, input().split())

MAP = [[0] * N for _ in range(N)]
fishbowls = list(map(int, input().split()))
ans = 0
# 최소 어항 1개 추가
while True:
    MAP = [[0] * N for _ in range(N)]
    find_min()
    stack()
    fish_move()
    make_arr()
    MAP = [[0] * N for _ in range(N)]
    fold()
    fish_move()
    make_arr()
    ans += 1
    if max(fishbowls) - min(fishbowls) <= K:
        break

print(ans)
