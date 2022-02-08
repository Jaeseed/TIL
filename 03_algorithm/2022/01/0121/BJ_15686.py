def dfs(step,list_, idx):
    if step == M:
        find_chicken_distance(list_)
        return
    for i in range(idx, chicken_cnt):
        dfs(step+1, list_ + [i], i+1)
    return


def find_chicken_distance(list_):
    global min_value
    value = 0
    for r in range(len(distance_list)):
        tmp_min = 2e29
        for c in range(len(list_)):
            tmp_min = min(tmp_min, distance_list[r][list_[c]])
        value += tmp_min
    min_value = min(min_value, value)
    return


N, M = map(int,input().split())
MAP = [list(map(int,input().split())) for _ in range(N)]
distance_list = []
for row in range(N):
    for col in range(N):
        if MAP[row][col] == 1:
            tmp = []
            for row_ in range(N):
                for col_ in range(N):
                    if MAP[row_][col_] == 2:
                        tmp.append(abs(row-row_) + abs(col-col_))
            distance_list.append(tmp)
chicken_cnt = len(distance_list[0])
min_value = 2e29
dfs(0,[],0)
print(min_value)