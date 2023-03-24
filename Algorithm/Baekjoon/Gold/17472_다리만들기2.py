from collections import deque
from heapq import heappop, heappush

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def numbering(ro, co):
    global visited, MAP
    qu = deque()
    qu.append([ro, co])
    while qu:
        r, c = qu.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr >= N or nr < 0 or nc >= M or nc < 0 or visited[nr][nc] or MAP[nr][nc] == 0: continue
            MAP[nr][nc] = island_cnt
            visited[nr][nc] = 1
            qu.append([nr, nc])
    return


def find_distance(ro, co, now_num):
    global visited, adj
    qu = deque()
    qu.append([ro, co])
    while qu:
        r, c = qu.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr >= N or nr < 0 or nc >= M or nc < 0 or visited[nr][nc]: continue
            # 바다일 때 다른 섬을 찾아 나서기
            if MAP[nr][nc] == 0:
                d = 0
                nr += dr[i]
                nc += dc[i]
                while 0 <= nr < N and 0 <= nc < M:
                    d += 1
                    # 현재 섬을 만날 때 break
                    if MAP[nr][nc] == now_num:
                        break
                    if MAP[nr][nc]:
                        if d > 1:
                            next_num = MAP[nr][nc]
                            adj[now_num][next_num] = min(d, adj[now_num][next_num])
                        break
                    nr += dr[i]
                    nc += dc[i]
            else:
                qu.append([nr, nc])
                visited[nr][nc] = 1
    return


def union(parent, son):
    global parent_list
    pp = find(parent)
    sp = find(son)
    if pp < sp:
        parent_list[sp] = pp
    else:
        parent_list[pp] = sp
    return


def find(now):
    global parent_list
    if parent_list[now] == now:
        return now
    p = find(parent_list[now])
    parent_list[now] = p
    return p


N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
# 총 섬의 개수
island_cnt = 0
# 1. 섬에 번호 매기기
visited = [[0] * M for _ in range(N)]
for n in range(N):
    for m in range(M):
        if MAP[n][m] and visited[n][m] == 0:
            island_cnt += 1
            visited[n][m] = 1
            MAP[n][m] = island_cnt
            numbering(n, m)
# 섬을 잇는 가중치가 최소인 간선 구하기
adj = [[100] * (island_cnt + 1) for _ in range(island_cnt + 1)]
visited = [[0] * M for _ in range(N)]
for n in range(N):
    for m in range(M):
        if MAP[n][m] and visited[n][m] == 0:
            visited[n][m] = 1
            find_distance(n, m, MAP[n][m])

heap = []
answer = 0
for f in range(island_cnt + 1):
    for s in range(f+1, island_cnt + 1):
        if adj[f][s] and adj[f][s] != 100:
            heappush(heap, [adj[f][s], f, s])
if heap:
    parent_list = list(range(island_cnt+1))
    while heap:
        distance, f, s = heappop(heap)
        # 사이클 돌 시에 continue
        if find(f) == find(s): continue
        union(f,s)
        answer += distance
    last_check = find(parent_list[1])
    for l in range(2, island_cnt + 1):
        if find(parent_list[l]) != last_check:
            answer = -1
            break
else:
    answer = -1
print(answer)
