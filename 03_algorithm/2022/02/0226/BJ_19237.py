import sys
import copy
dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]


def time_goes_on():
    global territory_list
    for r in range(N):
        for c in range(N):
            if territory_list[r][c][1]:
                territory_list[r][c][1] -= 1
                if territory_list[r][c][1] == 0:
                    territory_list[r][c] = [0,0]
    return


def odor_diffusion():
    global territory_list
    for r in range(N):
        for c in range(N):
            if MAP[r][c]:
                territory_list[r][c] = [MAP[r][c], k]
    return


def shark_move():
    global MAP, shark_direction
    tong = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if MAP[r][c]:
                now_shark = MAP[r][c]
                d = shark_direction[now_shark]
                cand = [-1,-1, -1]
                for i in range(4):
                    nd = priority[now_shark][d][i]
                    nr = r + dr[nd]
                    nc = c + dc[nd]
                    if nr >= N or nr < 0 or nc >= N or nc < 0: continue
                    if territory_list[nr][nc][0] == 0:
                        cand = [nr,nc,nd]
                        break
                    elif territory_list[nr][nc][0] == now_shark and cand[0] == -1:
                        cand = [nr,nc, nd]
                nr,nc,nd = cand
                if tong[nr][nc]:
                    tong[nr][nc] = min(tong[nr][nc], now_shark)
                else:
                    tong[nr][nc] = now_shark
                shark_direction[now_shark] = nd
    MAP = copy.deepcopy(tong)
    return


def check():
    for r in range(N):
        for c in range(N):
            if MAP[r][c] > 1:
                return False
    return True


N, M, k = map(int, input().split())
# 상어 위치
MAP = [list(map(int, input().split())) for _ in range(N)]
# 상어 냄새 영역
territory_list = [[[0, 0] for _ in range(N)] for _ in range(N)]
shark_direction = [0]
shark_direction += list(map(int,input().split()))
priority = [[[0,0,0,0] for _ in range(5)] for _ in range(M+1)]
cnt = 1
idx = 1
for m in range(M * 4):
    if cnt == 5:
        cnt = 1
        idx += 1
    priority[idx][cnt] = list(map(int,sys.stdin.readline().split()))
    cnt += 1
seconds = 0
while seconds < 1001:
    seconds += 1
    time_goes_on()
    odor_diffusion()
    shark_move()
    if check():
        break
if seconds == 1001:
    seconds = -1
print(seconds)