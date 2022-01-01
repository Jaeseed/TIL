from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    global bottom_list
    global visited
    qu = deque()
    qu.append([r, c])
    visited[r][c] = 1
    while qu:
        r, c = qu.popleft()
        if MAP[r + 1][c] == '.':
            bottom_list.append([r, c])
        for j in range(4):
            nr = r + dr[j]
            nc = c + dc[j]
            if nr < 0 or nc >= C or nc < 0 or MAP[nr][nc] == '.' or visited[nr][nc] == 1 or used[nr][nc] == 1: continue
            if nr == R-1:
                return True
            visited[nr][nc] = 1
            qu.append([nr, nc])
    return False


def find_min_cnt():
    min_cnt = 100
    for r,c in bottom_list:
        cnt = 0
        now_r = r+1
        while now_r < R:
            if visited[now_r][c] == 1:
                cnt = min_cnt
                break
            if MAP[now_r][c] == 'x': break
            now_r += 1
            cnt += 1
        min_cnt = min(min_cnt, cnt)
    return min_cnt


def gravity(jump):
    global used
    visited_col = [0] * C
    for r, c in bottom_list:
        if visited_col[c] == 1: continue
        visited_col[c] = 1
        for now_r in range(R-1,-1,-1):
            if MAP[now_r][c] == 'x' and visited[now_r][c] == 1:
                MAP[now_r + jump][c], MAP[now_r][c] = MAP[now_r][c], MAP[now_r + jump][c]
                used[now_r][c] = 1
    return


R, C = map(int, input().split())
MAP = [list(''.join(input())) for _ in range(R)]
N = int(input())
height_list = list(map(int, input().split()))
for n in range(N):
    row = R - height_list[n]
    if n % 2:
        for col in range(C-1, -1, -1):
            if MAP[row][col] == 'x':
                MAP[row][col] = '.'
                break
    else:
        for col in range(C):
            if MAP[row][col] == 'x':
                MAP[row][col] = '.'
                break
    cluster = []
    for i in range(4):
        new_row = row + dr[i]
        new_col = col + dc[i]
        if 0 <= new_row < R and 0 <= new_col < C and MAP[new_row][new_col] == 'x':
            if new_row == R - 1: continue
            cluster.append([new_row,new_col])
    visited = [[0] * C for _ in range(R)]
    used = [[0] * C for _ in range(R)]
    for cr, cc in cluster:
        if visited[cr][cc] == 0:
            visited = [[0] * C for _ in range(R)]
            bottom_list = []
            if bfs(cr, cc):
                continue
            else:
                des_cnt = find_min_cnt()
                if des_cnt > 0:
                    gravity(des_cnt)
for row in range(R):
    print(''.join(MAP[row]))