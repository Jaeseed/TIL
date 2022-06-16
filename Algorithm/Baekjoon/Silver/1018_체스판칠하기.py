import sys


def check(sr, sc, bow):
    global min_value
    units = ['', 'W', 'B']
    cnt = 0
    for r in range(sr, sr + 8):
        for c in range(sc, sc + 8):
            if MAP[r][c] != units[bow]:
                cnt += 1
            bow *= -1
        bow *= -1
        if cnt >= min_value:
            return
    min_value = min(min_value, cnt)
    return


N, M = map(int, input().split())
MAP = [list(sys.stdin.readline()) for _ in range(N)]
min_value = 2e29
for n in range(N - 7):
    for m in range(M - 7):
        check(n, m, 1)
        check(n, m, -1)
    if min_value == 0:
        break
print(min_value)

