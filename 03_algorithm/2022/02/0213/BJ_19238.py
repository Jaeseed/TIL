import sys
from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]


def find_person(r, c):
    visited = [[0] * N for _ in range(N)]
    visited[r][c] = 1
    qu = deque()
    qu.append([r, c, 0])
    while qu:
        r, c, fuel = qu.popleft()
        if F == fuel:
            return -1, -1, -1, -1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr >= N or nr < 0 or nc >= N or nc < 0 or visited[nr][nc] == 1 or MAP[nr][nc] == 1: continue
            if people_list[nr][nc] <= 0:
                visited[nr][nc] = 1
                qu.append([nr, nc, fuel + 1])
            else:
                return nr, nc, fuel + 1, people_list[nr][nc]
    return -1, -1, -1, -1


def find_goal(r, c, t):
    visited = [[0] * N for _ in range(N)]
    visited[r][c] = 1
    qu = deque()
    qu.append([r, c, 0])
    while qu:
        r, c, fuel = qu.popleft()
        if F == fuel:
            return -1, -1, -1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr >= N or nr < 0 or nc >= N or nc < 0 or visited[nr][nc] == 1 or MAP[nr][nc] == 1: continue
            if people_list[nr][nc] == -t:
                return nr, nc, fuel + 1
            visited[nr][nc] = 0
            qu.append([nr, nc, fuel + 1])
    return -1, -1, -1, -1


N, M, F = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
people_list = [[0] * N for _ in range(N)]
sr, sc = map(int, input().split())
sr -= 1
sc -= 1
complete_cnt = 0
for m in range(M):
    sr_, sc_, er_, ec_ = map(int, sys.stdin.readline().split())
    people_list[sr_ - 1][sc_ - 1] = m + 1
    people_list[er_ - 1][ec_ - 1] = -(m + 1)
while F != complete_cnt:
    total_used_fuel = 0
    if people_list[sr][sc] <= 0:
        sr, sc, used_fuel, target = find_person(sr, sc)
    else:
        used_fuel, target = 0, people_list[sr][sc]
    people_list[sr][sc] = 0
    if sr == -1:
        F = -1
        break
    F -= used_fuel
    sr, sc, used_fuel = find_goal(sr, sc, target)
    people_list[sr][sc] = 0
    if sr == -1:
        F = -1
        break
    F -= used_fuel
    F += used_fuel * 2
    complete_cnt += 1
    if M == complete_cnt:
        break
print(F)
