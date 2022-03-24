import sys

sys.stdin = open('input.txt', 'r')
from collections import deque

## 모든 방향을 기준 잡음
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

## 온풍기
def blowing(ro, co, d):
    visited = [[0] * C for _ in range(R)]
    # 온풍기 스타트점
    heat_tong[ro + dr[d]][co + dc[d]] += 5
    qu = deque()
    qu.append((ro + dr[d], co + dc[d], 4))
    # 방향별 for 구문 범위 지정
    idx = 0
    if d < 2:
        idx += 2
    while qu:
        r, c, plus = qu.popleft()
        if plus == 0:
            return
        sub_list = []
        if 0 <= r + dr[d] < R and 0 <= c + dc[d] < C:
            if visited[r][c] == 0:
                sub_list.append((r, c, plus))
                visited[r][c] = 1
            for i in range(idx, idx + 2):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < R and 0 <= nc < C and visited[nr][nc] == 0 and wall_MAP[r][c][i] == 0:
                    visited[nr][nc] = 1
                    sub_list.append((nr, nc, plus))
            for sr, sc, p in sub_list:
                if wall_MAP[sr][sc][d] == 0:
                    tmp_r, tmp_c = sr + dr[d], sc + dc[d]
                    heat_tong[tmp_r][tmp_c] += p
                    qu.append((tmp_r, tmp_c, p - 1))
    return


def make_change():
    for r in range(R):
        for c in range(C):
            heat_total[r][c] += heat_tong[r][c]
            heat_tong[r][c] = 0


def spread():
    for r in range(R):
        for c in range(C):
            for i in range(4):
                if wall_MAP[r][c][i] == 1: continue
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < R and 0 <= nc < C and heat_total[r][c] > heat_total[nr][nc]:
                    division = (heat_total[r][c] - heat_total[nr][nc]) // 4
                    heat_tong[nr][nc] += division
                    heat_tong[r][c] -= division
    return


def side_minus():
    for r in range(R):
        for c in range(C):
            if r == 0 or r == R - 1 or c == 0 or c == C - 1:
                if heat_total[r][c]:
                    heat_total[r][c] -= 1


def check_targets(value):
    for r, c in targets:
        if heat_total[r][c] < value:
            return False
    return True


R, C, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(R)]
W = int(input())
wall_MAP = [[[0, 0, 0, 0] for mm in range(C)] for _ in range(R)]

for w in range(W):
    row, col, t = map(int, input().split())
    # 벽 방향을 3차 리스트에 더함
    if t == 0:
        wall_MAP[row - 1][col - 1][2] = 1
        wall_MAP[row - 2][col - 1][3] = 1
    else:
        wall_MAP[row - 1][col - 1][0] = 1
        wall_MAP[row - 1][col][1] = 1
# 히터와 검사 공간 명단 선언
heater = []
targets = []
# 열 보관통
heat_total = [[0] * C for _ in range(R)]
heat_tong = [[0] * C for _ in range(R)]
# 초콜릿
chocolate = 0
# 히터와 검사할 공간 찾기
for row in range(R):
    for col in range(C):
        if 0 < MAP[row][col] < 5:
            heater.append([row, col, MAP[row][col] - 1])  # idx 맞추기 위해 -1
        elif MAP[row][col] == 5:
            targets.append([row, col])

while chocolate < 101:
    for heater_r, heater_c, direct in heater:
        blowing(heater_r, heater_c, direct)
    make_change()
    spread()
    make_change()
    side_minus()
    chocolate += 1
    if check_targets(K):
        break
print(chocolate)
