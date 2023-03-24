from collections import deque
import copy

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(sr, sc, step, walls):
    if step == 3:
        spread(walls)
        return
    # column이 끝까지 갔을 때 row + 1, column 초기화
    if sc == M:
        sr, sc = sr + 1, 0
    for r in range(sr, N):
        for c in range(sc, M):
            # 벽, 바이러스가 아닌 공간 체크
            if MAP[r][c] == 0:
                dfs(r, c + 1, step + 1, walls + [[r, c]])
        sc = 0
    return


def spread(walls):
    global answer
    visited = [[0] * M for _ in range(N)]
    # 임시 맵 생성
    tmp_map = copy.deepcopy(MAP)
    # 3개의 벽 맵에 갱신
    for wr, wc in walls:
        tmp_map[wr][wc] = 1
    # bfs로 바이러스 전부 확산
    for r in range(N):
        for c in range(M):
            if MAP[r][c] == 2:
                bfs(r, c, visited, tmp_map)
    cnt = 0
    # 청정 구역 수 계산
    for r in range(N):
        for c in range(M):
            if tmp_map[r][c] == 0:
                cnt += 1
    answer = max(answer, cnt)
    return


def bfs(ro, co, visited, tmp_map):
    qu = deque()
    qu.append([ro,co])
    visited[ro][co] = 1
    while qu:
        r, c = qu.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # (1) 맵 벗어나는 인덱스 방지, (2) 방문 체크, (3) 인접 구역의 청정 유무 체크
            if nr >= N or nr < 0 or nc >= M or nc < 0 or visited[nr][nc] or tmp_map[nr][nc] != 0: continue
            tmp_map[nr][nc] = 2
            qu.append([nr,nc])
            visited[nr][nc] = 1
    return


N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
answer = 0
dfs(0, 0, 0, [])
print(answer)