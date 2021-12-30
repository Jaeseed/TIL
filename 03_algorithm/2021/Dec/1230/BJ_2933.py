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
            if j == 1 and nr == R:
                return True
            if nr < 0 or nc >= C or nc < 0 or MAP[nr][nc] == '.' or visited[nr][nc] == 1: continue
            visited[nr][nc] = 1
            qu.append([nr, nc])
    return False


def find_min_cnt():
    min_cnt = 100
    for r,c in bottom_list:
        cnt = 0
        now_r = r
        while True:
            cnt += 1
            now_r += 1
            if now_r >= R or MAP[now_r][c] == 'x':
                break
        min_cnt = min(min_cnt, cnt)
    return min_cnt - 1


def gravity(jump):
    for r, c in bottom_list:
        now_r = r + jump
        while now_r-jump > 0:
            visited[now_r][c] = 1
            if MAP[now_r-jump][c] == 'x':
                MAP[now_r - jump][c], MAP[now_r][c] = MAP[now_r][c], MAP[now_r - jump][c]
                now_r -= 1
            else:
                jump += 1
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
    flag = 0
    visited = [[0] * C for _ in range(R)]
    for i in range(4):
        if i == 1: continue
        new_row = row + dr[i]
        new_col = col + dc[i]
        if MAP[new_row][new_col] == 'x' and visited[new_row][new_col] == 0:
            bottom_list = []
            if new_row == R - 1: continue
            if bfs(new_row, new_col):
                continue
            else:
                des_cnt = find_min_cnt()
                gravity(des_cnt)
for row in range(R):
    print(''.join(MAP[row]))