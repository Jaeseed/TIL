from collections import deque

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
    global MAP, ice_to_water, total
    # ice_to_water 추가할 값 저장 배열
    tong = [[0] * M for _ in range(N)]
    melted_ice_cnt = 0
    for r in range(N):
        for c in range(M):
            if MAP[r][c]:
                if MAP[r][c] - ice_to_water[r][c] <= 0:
                    # 빙산 총량 수정
                    total -= MAP[r][c]
                    MAP[r][c] = 0
                    melted_ice_cnt += 1
                    # 빙산이 다 녹은 구역일 시 인접한 구역의 ice_to_water 갱신
                    for i in range(4):
                        nr = r + dr[i]
                        nc = c + dc[i]
                        if MAP[nr][nc] == 0: continue
                        tong[nr][nc] += 1
                else:
                    MAP[r][c] -= ice_to_water[r][c]
    # ice_to_water 값 갱신
    for r in range(N):
        for c in range(N):
            ice_to_water[r][c] += tong[r][c]
    return melted_ice_cnt


def check_area(r,c):
    global visited
    qu = deque()
    qu.append([r,c])
    while qu:
        r, c = qu.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if MAP[nr][nc] == 0 or visited[nr][nc]: continue
            qu.append([nr,nc])
            visited[nr][nc] = 1


N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
# 전체 시간
years = 0
# 빙산 높이 총합
total = 0
# 각 칸마다 녹는 양 저장하는 배열
ice_to_water = [[0] * M for _ in range(N)]
# total 값, ice_to_water 값 최초 설정
for n in range(1,N-1):
    for m in range(1,M-1):
        if MAP[n][m]:
            total += MAP[n][m]
            search_water(n, m)

# 빙산 구역이 2개 이상이거나, 빙산이 다 녹을 때까지 while문 반복
while True:
    years += 1
    # 빙산 녹임
    ret = melt()
    if ret == 0:
        continue
    visited = [[0] * M for _ in range(N)]
    # 빙산 구역 개수
    area_cnt = 0
    for n in range(N):
        for m in range(M):
            if MAP[n][m] and visited[n][m] == 0:
                check_area(n,m)
                area_cnt += 1
    # 구역이 2개 이상일 때 종료
    if area_cnt > 1:
        break
    # 남은 빙산 확인
    if total == 0:
        years = 0
        break
print(years)