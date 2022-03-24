import sys

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]


def spring():
    global MAP
    global nutrient
    global parents_list
    global tree_cnt
    for r in range(N):
        for c in range(N):
            for k in range(len(MAP[r][c])):
                if MAP[r][c][k] <= nutrient[r][c]:
                    nutrient[r][c] -= MAP[r][c][k]
                    MAP[r][c][k] += 1
                    if MAP[r][c][k] % 5 == 0:
                        parents_list[r][c] += 1
                else:
                    pop_cnt = len(MAP[r][c]) - k
                    now_cnt = 0
                    while now_cnt < pop_cnt:
                        dead_tree = MAP[r][c].pop()
                        tree_cnt -= 1
                        if tree_cnt == 0:
                            return
                        nutrient[r][c] += dead_tree // 2
                        now_cnt += 1
                    break
    return


def fall():
    global tree_cnt
    for r in range(N):
        for c in range(N):
            if parents_list[r][c]:
                while parents_list[r][c] > 0:
                    parents_list[r][c] -= 1
                    for i in range(8):
                        nr = r + dr[i]
                        nc = c + dc[i]
                        if nr >= N or nr < 0 or nc >= N or nc < 0: continue
                        MAP[nr][nc].insert(0, 1)
                        tree_cnt += 1
    return


def winter():
    global nutrient
    for r in range(N):
        for c in range(N):
            nutrient[r][c] += A[r][c]
    return


N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
MAP = [[[] for _ in range(N)] for _ in range(N)]
nutrient = [[5] * N for _ in range(N)]
parents_list = [[0] * N for _ in range(N)]
tree_cnt = 0
for m in range(M):
    x, y, z = map(int, sys.stdin.readline().split())
    MAP[x-1][y-1].append(z)
    tree_cnt += 1
for row in range(N):
    for col in range(N):
        if len(MAP[row][col]) > 1:
            MAP[row][col].sort()
year = 0

while year < K:
    spring()
    if tree_cnt == 0:
        break
    fall()
    winter()
    year += 1
print(tree_cnt)