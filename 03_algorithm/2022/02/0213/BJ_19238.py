import sys
from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]


def find_client(r, c):
    qu = deque()
    qu.append([r, c, 0])
    visited = [[0] * N for _ in range(N)]
    visited[r][c] = 1
    tong = []
    now_fuel = 0
    while qu:
        r, c, fuel = qu.popleft()
        if fuel == F:
            return -1, -1, -1, -1
        if now_fuel != fuel:
            mr, mc, real_t = 20,20,0
            if tong:
                for t_ in range(len(tong)):
                    if mr > tong[t_][0]:
                        mr, mc, real_t = tong[t_][0], tong[t_][1], tong[t_][2]
                    elif mr == tong[t_][0] and mc > tong[t_][0]:
                        mr, mc, real_t = tong[t_][0], tong[t_][1], tong[t_][2]
                for e in range(len(people_list[mr][mc])):
                    if people_list[mr][mc][e] == real_t:
                        people_list[mr][mc][e] = 0
                        break
                return mr, mc, fuel, real_t
            now_fuel += 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr >= N or nr < 0 or nc >= N or nc < 0 or visited[nr][nc] == 1 or MAP[nr][nc] == 1: continue
            if people_list[nr][nc]:
                for p_ in range(len(people_list[nr][nc])):
                    if people_list[nr][nc][p_] > 0:
                        tong.append([nr, nc, people_list[nr][nc][p_]])
            qu.append([nr, nc, fuel + 1])
            visited[nr][nc] = 1
    return -1, -1, -1, -1


def find_goal(r, c, t):
    qu = deque()
    qu.append([r, c, 0])
    visited = [[0] * N for _ in range(N)]
    visited[r][c] = 1
    while qu:
        r, c, fuel = qu.popleft()
        if fuel == F:
            return -1, -1, -1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr >= N or nr < 0 or nc >= N or nc < 0 or visited[nr][nc] == 1 or MAP[nr][nc] == 1: continue
            if people_list[nr][nc]:
                for p_ in range(len(people_list[nr][nc])):
                    if people_list[nr][nc][p_] == -t:
                        people_list[nr][nc][p_] = 0
                        return nr, nc, fuel + 1
            qu.append([nr, nc, fuel + 1])
            visited[nr][nc] = 1
    return -1, -1, -1


N, M, F = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
people_list = [[[] for _ in range(N)] for _ in range(N)]
sr, sc = map(int, input().split())
sr -= 1
sc -= 1
for m in range(M):
    sr_, sc_, er_, ec_ = map(int, sys.stdin.readline().split())
    people_list[sr_ - 1][sc_ - 1].append(m + 1)
    people_list[er_ - 1][ec_ - 1].append(-(m + 1))
completed_cnt = 0
while completed_cnt < M:
    target = 0
    used_fuel = 0
    if people_list[sr][sc]:
        for p in range(len(people_list[sr][sc])):
            if people_list[sr][sc][p] > 0:
                target = people_list[sr][sc][p]
                people_list[sr][sc][p] = 0
                break
    if target == 0:
        sr, sc, used_fuel, target = find_client(sr, sc)
    if sr == -1:
        F = -1
        break
    F -= used_fuel
    sr, sc, used_fuel = find_goal(sr, sc, target)
    if sr == -1:
        F = -1
        break
    F += used_fuel
    completed_cnt += 1
print(F)
