## 알고리즘 출제 연습
import sys

sys.stdin = open('input.txt', 'r')

from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def find_facilities(row, col, house_idx):
    # 방문 체크
    visited = [[0] * M for _ in range(N)]
    visited[row][col] = 1
    qu_tmp = deque()
    qu_tmp.append((row, col, 0))
    while qu_tmp:
        r, c, distance = qu_tmp.popleft()
        if distance == 2:
            continue
        for d in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr >= N or nr < 0 or nc >= M or nc < 0 or visited[nr][nc] == 1: continue
            if ord('B') <= ord(MAP[nr][nc]) <= ord('M'):
                score[house_idx] += 1
            elif ord('N') <= ord(MAP[nr][nc]) <= ord('Y'):
                score[house_idx] -= 1
            visited[nr][nc] = 1
            qu_tmp.append((nr, nc, distance + 1))


def find_min_distance(row, col, house_num):
    visited = [0 * house_cnt]
    graph = [[0] * house_cnt]
    min_dist = (abs(goal_r-row) + abs(goal_c-col)) * 30


## 변수 받기
M, N, n, m  = map(int, input().split())
MAP = [list(input().split()) for _ in range(N)]
## 집 매물 입력 받기
house_cnt = int(input())
monthly_fee = list(map(int, input().split()))
## 지하철 노선도 및 비용 변수 선언
subway_cnt = int(input())
subway_list = []
subway_cost = []
## 지하철 노선 입력 받기
for i in range(subway_cnt):
    subway_list.append(map(int, input().split()))
    subway_cost.append(list(map(int, input().split())))
## 회사 좌표 찾기
for r in range(N):
    for c in range(M):
        if MAP[n][m] == 'A':
            goal_r = n
            goal_c = m

score = [100 * house_cnt]
## 월세 점수 차감
for h in range(house_cnt):
    score[h] -= monthly_fee[h]// n

for r in range(N):
    for c in range(M):
        if MAP[r][c].isdigit() and MAP[r][c] != '0':
            find_facilities(r, c, int(MAP[r][c]) - 1)  ## 집 번호가 순서대로인지
            find_min_distance(r, c, int(MAP[r][c]))