import sys

dr = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dc = [0, -1, -1, 0, 1, 1, 1, 0, -1]


def move_cloud(d_, s_):
    global A, cloud
    tmp = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if cloud[r][c] == 1:
                nr = r + dr[d_] * s_
                nc = c + dc[d_] * s_
                nr %= N
                nc %= N
                tmp[nr][nc] = 1
    for r in range(N):
        for c in range(N):
            if tmp[r][c]:
                A[r][c] += 1
                cloud[r][c] = -1
            else:
                cloud[r][c] = 0
    return


def copy_water():
    global A
    tong = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if cloud[r][c] >= 0: continue
            cnt = 0
            for i in range(2, 9, 2):
                nr = r + dr[i]
                nc = c + dc[i]
                if nr >= N or nr < 0 or nc >= N or nc < 0 or A[nr][nc] == 0: continue
                cnt += 1
            tong[r][c] += cnt
    for r in range(N):
        for c in range(N):
            A[r][c] += tong[r][c]
    return


def make_cloud():
    global A, cloud
    for r in range(N):
        for c in range(N):
            if A[r][c] >= 2 and cloud[r][c] == 0:
                A[r][c] -= 2
                cloud[r][c] = 1
    return


N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

cloud = [[0] * N for _ in range(N)]
cloud[N - 1][0], cloud[N - 1][1], cloud[N - 2][0], cloud[N - 2][1] = 1, 1, 1, 1
for m in range(M):
    d, s = map(int, sys.stdin.readline().split())
    move_cloud(d,s)
    copy_water()
    make_cloud()

total_water = 0
for r_ in range(N):
    for c_ in range(N):
        total_water += A[r_][c_]
print(total_water)