dr = [1, -1]
dc = [-1, 1]


def choose(r, c, step):
    global now_max, visited
    if step == N:
        now_max = max(now_max, sum(visited))
        return
    if N - step + sum(visited) <= now_max:
        return
    for unit in (-1, 1):
        idx = 0
        while True:
            nr = r - idx
            nc = c + idx
            if nr >= N or nr < 0 or nc >= N or nc < 0:
                break
            if visited[idx] or MAP[nr][nc] == 0:
                idx += unit
                continue
            visited[idx] = 1
            choose(r + 1, c + 1, step + 1)
            visited[idx] = 0
            idx += unit
    choose(r + 1, c + 1, step + 1)
    return


N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
answer = 0
now_max = 0
visited = [0] * 10
if MAP[0][0] or MAP[-1][-1]:
    visited[0] = 1
choose(0, 0, 1)
answer += now_max
now_max = 0
visited = [0] * 10
choose(1, 0, 1)
answer += now_max
print(answer)