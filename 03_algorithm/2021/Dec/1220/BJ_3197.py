from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def find_friend(sr, sc, er, ec):
    visited = [[0] * C for _ in range(R)]
    visited[sr][sc] = 1
    qu = deque()
    qu.append([sr, sc])
    while qu:
        r, c = qu.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr >= R or nr < 0 or nc >= C or nc < 0 or visited[nr][nc] == 1 or MAP[nr][nc] == 'X': continue
            if nr == er and nc == ec:
                return True
            visited[nr][nc] = 1
            qu.append([nr, nc])
    return False


R, C = map(int, input().split())
MAP = [list(' '.join(input()).split()) for _ in range(R)]
days = 0
dist_check = [[[0, 0] for _ in range(C)] for p in range(R)]
birds = []
for row in range(R):
    for col in range(C):
        if MAP[row][col] == 'L':
            birds.append([row, col])
find_friend(birds[0][0], birds[0][1], birds[1][0], birds[1][1])
print(days)
