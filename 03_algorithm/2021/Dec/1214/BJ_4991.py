from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(sr, sc, er, ec):
    qu = deque()
    qu.append([sr, sc, 0])
    visited = [[0] * w in range(h)]
    while qu:
        row, col, cnt = qu.popleft()
        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]
            if nr >= h or nr < 0 or nc >= w or nc < 0 or visited[nr][nc] == 1 or MAP[nr][nc] == 'x': continue
            if nr == er and nc == ec:
                return cnt + 1
            qu.append([nr, nc, cnt + 1])
    return -1
def calculate_min_distance():
    min_distance = 2e29



w, h = map(int, input().split())
MAP = [' '.join(input()).split() for _ in range(h)]
dust_tong = []
for r in range(h):
    for c in range(w):
        if MAP[r][c] == '*':
            dust_tong.append([r, c])
        if MAP[r][c] == 'o':
            MAP[r][c] = '.'
            cleaner = [r, c]
dusts_cnt = len(dust_tong)
ans = 0
adj = [[0] * dusts_cnt for _ in range(dusts_cnt)]
for d in range(dusts_cnt):
    row, col = dust_tong[d][0], dust_tong[d][0]
    start_r, start_c = cleaner[0], cleaner[1]
    result = bfs(start_r, start_c, row, col)
    if result == -1:
        ans = -1
        break
    else:
        adj[0][d + 1], adj[d + 1][0] = result, result
if ans == 0:
    for start in range(dusts_cnt):
        start_r, start_c = dust_tong[start][0], dust_tong[start][1]
        for end in range(dusts_cnt):
            if start == end: continue
            end_r, end_c = dust_tong[end][0], dust_tong[end][1]
            result = bfs(start_r, start_c, end_r, end_c)
            adj[start + 1][end + 1], adj[end + 1][start + 1] = result, result
    calculate_min_distance()

else:
    print(-1)

# from collections import deque
#
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
#
# def bfs():
#     global dusts
#     global visited
#     qu = deque()
#     row, col = cleaner[0], cleaner[1]
#     visited[row][col] = 1
#     qu.append([row, col, 0, 0])
#     while qu:
#         row, col, distance, cnt = qu.popleft()
#         if cnt == dusts:
#             return distance
#         for i in range(4):
#             nr = row + dr[i]
#             nc = col + dc[i]
#             if nr >= h or nr < 0 or nc >= w or nc < 0 or visited[nr][nc] == 1 or MAP[nr][nc] == 'x':
#                 continue
#             if MAP[nr][nc] != '*':
#                 qu.append([nr,nc, distance + 1, cnt])
#                 visited[nr][nc] = 1
#                 continue
#             else:
#                 MAP[nr][nc] = '.'
#                 qu = deque()
#                 qu.append([nr, nc, distance + 1, cnt + 1])
#                 visited = [[0] * w for _ in range(h)]
#                 visited[nr][nc] = 1
#                 break
#     return -1
#
#
# w, h = map(int, input().split())
# MAP = [' '.join(input()).split() for _ in range(h)]
# zero1, zero2 = map(int,input().split())
# dusts = 0
# for r in range(h):
#     for c in range(w):
#         if MAP[r][c] == '*':
#             dusts += 1
#         if MAP[r][c] == 'o':
#             MAP[r][c] = '.'
#             cleaner = [r, c]
# visited = [[0] * w for _ in range(h)]
# ans = bfs()
# print(ans)
