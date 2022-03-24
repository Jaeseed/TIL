import sys
dr = [-1,1,0,0]
dc = [0,0,-1,1]


def rotate(x_, d_, k_):
    global MAP
    tmp = [0] * M
    if d_ == 0:
        for i in range(M):
            tmp[(i+k_) % M] = MAP[x_][i]
    else:
        for i in range(M):
            tmp[i] = MAP[x_][(i+k_) % M]
    MAP[x_] = tmp[:]
    return


def adj_check():
    global MAP
    global is_checked
    global all_cnt
    global M
    flag_ = 0
    tong = []
    for r in range(N):
        for c in range(M):
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if nr >= N or nr < 0: continue
                if nc < 0:
                    nc += M
                elif nc >= M:
                    nc -= M
                if is_checked[nr][nc] == 1 or MAP[nr][nc] == 0: continue
                if MAP[r][c] == MAP[nr][nc]:
                    is_checked[nr][nc] = 1
                    if not tong:
                        tong.append((r,c))
            if tong:
                tr, tc = tong.pop()
                is_checked[tr][tc] = 1
                flag_ = 1
    if flag_:
        return True
    return False


def make_them_average():
    global MAP
    cnt = 0
    total = 0
    for r in range(N):
        for c in range(M):
            if MAP[r][c]:
                cnt += 1
                total += MAP[r][c]
    avg = total / cnt
    for r in range(N):
        for c in range(M):
            if MAP[r][c]:
                if MAP[r][c] > avg:
                    MAP[r][c] -= 1
                elif MAP[r][c] < avg:
                    MAP[r][c] += 1
    return


N, M, T = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
all_cnt = N * M
for t in range(T):
    x, d, k = map(int, sys.stdin.readline().split())
    now = 1
    nx = x
    while nx - 1 < N:
        rotate(nx-1, d, k)
        now += 1
        nx = now * x
    is_checked = [[0] * M for _ in range(N)]
    flag = 0
    if adj_check():
        for row in range(N):
            for col in range(M):
                if is_checked[row][col]:
                    MAP[row][col] = 0
                    all_cnt -= 1
                    flag = 1
    if flag == 0:
        make_them_average()
    if all_cnt == 0:
        break
total_ = 0
for row in range(N):
    for col in range(M):
        total_ += MAP[row][col]
print(total_)
