import sys

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]


def move_fireball():
    global MAP,repeated_fire, tong
    for r in range(N):
        for c in range(N):
            if repeated_fire[r][c] == 2:
                m_, s_, d_ = MAP[r][c]
                repeated_fire[r][c] = 0
                if MAP[r][c][2] >= 0:
                    for i in range(0,8,2):
                        nr = r + dr[i] * s_
                        nc = c + dc[i] * s_
                        nr %= N
                        nc %= N
                        check_tong(nr,nc,m_,s_,i)
                else:
                    for i in range(1, 8, 2):
                        nr = r + dr[i] * s_
                        nc = c + dc[i] * s_
                        nr %= N
                        nc %= N
                        check_tong(nr, nc, m_, s_, i)
            elif MAP[r][c]:
                m_,s_,d_ = MAP[r][c]
                nr = r + dr[d_] * s_
                nc = c + dc[d_] * s_
                nr %= N
                nc %= N
                check_tong(nr, nc, m_, s_, d_)
    for r in range(N):
        for c in range(N):
            if repeated_fire[r][c]:
                cnt = repeated_fire[r][c]
                tong[r][c][0] //= 5
                tong[r][c][1] //= cnt
                if tong[r][c][0] == 0:
                    tong[r][c] = 0
    for r in range(N):
        for c in range(N):
            MAP[r][c] = tong[r][c]
    return


def check_tong(nr,nc,mm,ss,dd):
    global tong
    if tong[nr][nc]:
        if tong[nr][nc][2] % 2 == dd % 2:
            tong[nr][nc][0] += mm
            tong[nr][nc][1] += ss
            repeated_fire[nr][nc] = 1
        else:
            tong[nr][nc][0] += mm
            tong[nr][nc][1] += ss
            tong[nr][nc][2] = -1
            repeated_fire[nr][nc] = 1
    else:
        tong[nr][nc] = [mm, ss, dd]
    return


N, M, K = map(int, input().split())
MAP = [[0] * N for _ in range(N)]
for m in range(M):
    repeated_fire = [[0] * N for _ in range(N)]
    is_splited = [[0] * N for _ in range(N)]
    r_, c_, m, s, d = map(int, sys.stdin.readline().split())
    r_ -= 1
    c_ -= 1
    MAP[r_][c_] = [m, s, d]
turns = 0
while turns < K:
    turns += 1
    tong = [[0] * N for _ in range(N)]
    move_fireball()
    for r_ in range(N):
        for c_ in range(N):
            if repeated_fire[r_][c_]:
                repeated_fire[r_][c_] = 2
total_mass = 0
for r_ in range(N):
    for c_ in range(N):
        if MAP[r_][c_]:
            if repeated_fire[r_][c_]:
                total_mass += MAP[r_][c_][0] * 4
            else:
                total_mass += MAP[r_][c_][0]
print(total_mass)
