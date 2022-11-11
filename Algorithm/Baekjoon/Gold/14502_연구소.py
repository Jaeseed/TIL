from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def choose_three(now, step, chosen_list):
    if step == 3:
        bfs(chosen_list)
        return
    for i in range(now, len(possible_spot)):
        choose_three(i+1, step+1, chosen_list + [possible_spot[i]])


def bfs(chosen_list):
    global MAP, answer
    for r,c in chosen_list:
        MAP[r][c] = 1
    infected_cnt = 0
    qu = deque(virus_list)
    visited = [[0] * M for _ in range(N)]
    while qu:
        r, c = qu.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr >= N or nr < 0 or nc >= M or nc < 0 or visited[nr][nc] or MAP[nr][nc]: continue
            visited[nr][nc] = 1
            qu.append([nr,nc])
            infected_cnt += 1
    answer = max(answer, empty_cnt - infected_cnt - 3)
    for r, c in chosen_list:
        MAP[r][c] = 0
    return


N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
answer = 0
empty_cnt = 0
virus_list = []
possible_spot = []
for n in range(N):
    for m in range(M):
        if MAP[n][m] == 0:
            empty_cnt += 1
            possible_spot.append([n, m])
        elif MAP[n][m] == 2:
            virus_list.append([n,m])
else:
    choose_three(0, 0, [])
print(answer)