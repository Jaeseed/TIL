from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(row, col):
    global opened_cnt
    global all_visited
    qu = deque()
    qu.append([row, col, 0])
    # 각 인원의 방문 체크
    visited = [[0] * (C+2) for _ in range(R+2)]
    visited[row][col] = 1
    all_visited[row][col] = 1
    while qu:
        r, c, cnt = qu.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr >= (R+2) or nr < 0 or nc >= (C+2) or nc < 0 or MAP[nr][nc] == '*' or visited[nr][nc] == 1: continue
            visited[nr][nc] = 1
            all_visited[nr][nc] = 1
            # 문일 때 cnt + 1
            if MAP[nr][nc] == '#':
                qu.append([nr,nc,cnt+1])
                opened_cnt[nr][nc] += cnt+1
            else:
                qu.appendleft([nr,nc,cnt])
                opened_cnt[nr][nc] += cnt
    return


T = int(input())
for t in range(T):
    R, C = map(int, input().split())
    # 리스트 가장자리 한줄씩 더하기
    MAP = [['.'] * (C+2)]
    for h in range(R):
        MAP.append(list('.' + input() + '.'))
    MAP.append(['.'] * (C+2))
    all_visited = [[0] * (C+2) for _ in range(R+2)]
    opened_cnt = [[0] * (C+2) for _ in range(R+2)]
    # 상근이 방문 체크
    bfs(0, 0)
    for h in range(1,R+1):
        for w in range(1,C+1):
            if MAP[h][w] == '$':
                # 죄수 방문 체크
                bfs(h, w)
    min_opened_cnt = 2e29
    # 문에서의 최소값 구하기
    for h in range(1,R+1):
        for w in range(1,C+1):
            if MAP[h][w] == '#':
                min_opened_cnt = min(min_opened_cnt, opened_cnt[h][w]-2)
            elif all_visited[h][w] == 1:
                min_opened_cnt = min(min_opened_cnt, opened_cnt[h][w])
    print(min_opened_cnt)
