dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]


def move(r, c, d):
    while 0 <= r < N and 0 <= c < M:
        if MAP[r][c]:
            d = (d + 2) % 4
        r += dr[d]
        c += dc[d]
    if d == 0:
        ret = N + c + 1
    elif d == 1:
        ret = 2 * N + 2 * M - c
    elif d == 2:
        ret = r + 1
    else:
        ret = N + M + N - r
    return ret


N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
answer = []
# 1. 좌측 빛
for i in range(N):
    answer.append(move(i, 0, 3))


# 2. 하단 빛
for i in range(M):
    answer.append(move(N-1, i, 1))

# 3. 우측 빛
for i in range(N-1, -1, -1):
    answer.append(move(i, M-1, 2))

# 4. 상단 빛
for i in range(M-1, -1, -1):
    answer.append(move(0, i, 0))
print(*answer)
