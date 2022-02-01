def dfs(list_):
    if min_gap == 0:
        return
    if len(list_) == 2:
        start_spot(list_)
        return
    for i in range(1,N-1):
        if list_:
            if i + list_[0] >= N: continue
        list_.append(i)
        dfs(list_)
        list_.pop()
    return


def start_spot(list_):
    d1, d2 = list_[0], list_[1]
    for r in range(N-d1-d2):
        for c in range(d1,N-d2):
            if min_gap == 0:
                return
            region_selection(r,c,d1,d2)
    return


def region_selection(r,c,d1,d2):
    global min_gap
    region_population_list = [0,0,0,0,0]
    for r_ in range(N):
        for c_ in range(N):
            if r_ < r and c_ <= c + d1:
                region_population_list[0] += population_list[r_][c_]
            elif r_ <= r and c_ > c + d1:
                region_population_list[1] += population_list[r_][c_]
            elif r_ >= r and c_ < c + d1:
                region_population_list[2] += population_list[r_][c_]
            elif r_ > r and c_ >= c + d1:
                region_population_list[3] += population_list[r_][c_]
            else:
                region_population_list[4] += population_list[r_][c_]
    min_gap = min(min_gap, max(region_population_list)- min(region_population_list))
    return


N = int(input())
population_list = [list(map(int, input().split())) for _ in range(N)]
min_gap = 2e29
dfs([])
print(min_gap)