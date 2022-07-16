def dfs(r, c, length):
    global cnt
    if length == 1:
        cnt[paper[r][c]] += 1
        return
    num = paper[r][c]
    if check(r, c, length, num):
        cnt[num] += 1
    else:
        length //= 3
        for n in range(3):
            for m in range(3):
                dfs(r + length * n, c + length * m, length)
    return


def check(r, c, length, num):
    global paper
    for n in range(r, r + length):
        for m in range(c, c + length):
            if paper[n][m] != num:
                return False
    return True

N = int(input())
cnt = [0] * 3
paper = [list(map(int, input().split())) for _ in range(N)]
dfs(0, 0, N)
for i in range(-1,2):
    print(cnt[i])