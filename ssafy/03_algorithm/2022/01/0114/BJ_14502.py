from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def make_wall(nr, nc, step):
    global MAP
    if step == 3:
        find_safe_zone()
        return
    for r in range(nr, R):
        if r == nr:
            range_c = nc
        else:
            range_c = 0
        for c in range(range_c, C):
            if MAP[r][c] == 0:
                MAP[r][c] = -1
                if c < C-1:
                    make_wall(r, c+1, step + 1)
                else:
                    make_wall(r+1, 0, step + 1)
                MAP[r][c] = 0
    return


def find_safe_zone():
    global max_safe_zone
    cnt = 0
    visited = [[0] * C for _ in range(R)]
    for virus in virus_list:
        r, c = virus[0], virus[1]
        visited[r][c] = 1
    for virus in virus_list:
        r, c = virus[0], virus[1]
        qu = deque()
        qu.append([r,c])
        while qu:
            r, c = qu.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < R and 0 <= nc < C and MAP[nr][nc] == 0 and visited[nr][nc] == 0:
                    qu.append([nr,nc])
                    cnt += 1
                    visited[nr][nc] = 1
                    if safe_zone - cnt - 3 <= max_safe_zone:
                        return
    now_safe_zone = safe_zone - cnt
    if max_safe_zone < now_safe_zone-3:
        max_safe_zone = now_safe_zone - 3
    return


R, C = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(R)]
safe_zone = 0
virus_list = []
for row in range(R):
    for col in range(C):
        if MAP[row][col] == 0:
            safe_zone += 1
        elif MAP[row][col] == 2:
            virus_list.append([row, col])
max_safe_zone = 0
make_wall(0,0,0)
print(max_safe_zone)