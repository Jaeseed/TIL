from collections import deque
import sys

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# ice_to_water 값 최초 설정
def search_water(r, c):
    global ice_to_water
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if MAP[nr][nc]: continue
        ice_to_water[r][c] += 1
    return


# ice_to_water 값에 따라 빙산 녹이는 함수
def melt():
    global MAP, ice_to_water, total_height
    # ice_to_water 추가할 값 저장 배열
    tong = [[0] * M for _ in range(N)]
    melted_ice_cnt = 0
    for r in range(1, N - 1):
        for c in range(1, M - 1):
            if MAP[r][c]:
                if MAP[r][c] - ice_to_water[r][c] <= 0:
                    # 빙산 총량 수정
                    total_height -= MAP[r][c]
                    MAP[r][c] = 0
                    melted_ice_cnt += 1
                    # 빙산이 다 녹은 구역일 시 인접한 구역의 ice_to_water 갱신
                    for i in range(4):
                        nr = r + dr[i]
                        nc = c + dc[i]
                        if MAP[nr][nc] == 0: continue
                        tong[nr][nc] += 1
                else:
                    total_height -= ice_to_water[r][c]
                    MAP[r][c] -= ice_to_water[r][c]
    # ice_to_water 값 갱신
    for r in range(1, N - 1):
        for c in range(1, M - 1):
            ice_to_water[r][c] += tong[r][c]
    return melted_ice_cnt


def check_area():
    global all_cnt
    for r in range(1, N - 1):
        for c in range(1, M - 1):
            if MAP[r][c]:
                now_cnt = bfs(r, c)
                if all_cnt == now_cnt:
                    return True
                return False


def bfs(r, c):
    cnt = 0
    visited = [[0] * M for _ in range(N)]
    qu = deque()
    qu.append([r, c])
    while qu:
        r, c = qu.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if MAP[nr][nc] == 0 or visited[nr][nc]: continue
            qu.append([nr, nc])
            visited[nr][nc] = 1
            cnt += 1
    return cnt


N, M = map(int, input().split())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 전체 시간
years = 0
# 빙산 높이 총합
total_height = 0
# 전체 빙산 개수
all_cnt = 0
# 각 칸마다 녹는 양 저장하는 배열
ice_to_water = [[0] * M for _ in range(N)]
# total 값, ice_to_water 값 최초 설정
for n in range(1, N - 1):
    for m in range(1, M - 1):
        if MAP[n][m]:
            total_height += MAP[n][m]
            all_cnt += 1
            search_water(n, m)

# 빙산 구역이 2개 이상이거나, 빙산이 다 녹을 때까지 while문 반복
while True:
    years += 1
    # 빙산 녹임
    melted_ice = melt()
    # 빙산 안 녹았을 때 continue
    if melted_ice == 0:
        continue
    all_cnt -= melted_ice
    # 남은 빙산 확인
    if all_cnt == 0:
        years = 0
        break
    ret = check_area()
    # 구역이 2개 이상일 때 종료
    if not ret:
        break
print(years)