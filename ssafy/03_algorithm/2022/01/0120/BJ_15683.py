dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def dfs(step, rotate_list):
    if step == cctv_cnt:
        observation(rotate_list)
        return
    for i in range(4):
        dfs(step + 1, rotate_list + str(i))


def observation(rotate_list):
    global ans
    cnt = 0
    visited = [[0] * M for _ in range(N)]
    for i in range(cctv_cnt):
        r, c, num_cctv = cctv_list[i]
        idx = int(rotate_list[i])
        for j in range(4):
            if cctv_direction[num_cctv][j] == 0: continue
            dr_ = dr[(idx + j) % 4]
            dc_ = dc[(idx + j) % 4]
            nr, nc = r, c
            while True:
                nr += dr_
                nc += dc_
                if nr >= N or nr < 0 or nc >= M or nc < 0 or MAP[nr][nc] == 6: break
                if MAP[nr][nc] == 0 and visited[nr][nc] == 0:
                    cnt += 1
                    visited[nr][nc] = 1
    ans = min(ans, blind_spot_cnt - cnt)
    return



N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
cctv_list = []
blind_spot_cnt = 0
ans = 2e29
for row in range(N):
    for col in range(M):
        if 1 <= MAP[row][col] <= 5:
            cctv_list.append([row, col, MAP[row][col]])
        elif MAP[row][col] == 0:
            blind_spot_cnt += 1
cctv_cnt = len(cctv_list)
cctv_direction = [[0], [1, 0, 0, 0], [1, 0, 1, 0], [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 1]]
dfs(0, '')
print(ans)