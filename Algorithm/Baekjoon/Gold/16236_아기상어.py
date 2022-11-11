from collections import deque

dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]


def find_shark():
    global MAP
    for row in range(N):
        for col in range(N):
            if MAP[row][col] == 9:
                MAP[row][col] = 0
                return row, col


def predation():
    global shark_r, shark_c, MAP
    qu = deque()
    qu.append([shark_r, shark_c, 0])
    visited = [[0] * N for _ in range(N)]
    visited[shark_r][shark_c] = 1
    flag = 0
    flag_cnt = 0
    cand_r, cand_c = 0,0
    while qu:
        r, c, cnt = qu.popleft()
        if flag == 1 and flag_cnt < cnt:
            shark_r = cand_r
            shark_c = cand_c
            MAP[shark_r][shark_c] = 0
            return cnt
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr >= N or nr < 0 or nc >= N or nc < 0 or visited[nr][nc] or MAP[nr][nc] > shark_level[0]: continue
            if 0 < MAP[nr][nc] < shark_level[0]:
                if flag == 0:
                    cand_r = nr
                    cand_c = nc
                    flag = 1
                    flag_cnt = cnt
                else:
                    if cand_r > nr:
                        cand_r, cand_c = nr,nc
                    elif cand_r == nr:
                        if cand_c > nc:
                            cand_r, cand_c = nr,nc
            qu.append([nr,nc,cnt+1])
            visited[nr][nc] = 1
    return -1


N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
# [크기, 먹은 수]
shark_level = [2, 0]
shark_r, shark_c = find_shark()
answer = 0
while True:
    ret = predation()
    if ret == -1:
        break
    shark_level[1] += 1
    if shark_level[0] == shark_level[1]:
        shark_level[0] += 1
        shark_level[1] = 0
    answer += ret
print(answer)
