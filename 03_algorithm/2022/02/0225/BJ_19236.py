import copy

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]


def dfs(food_cnt):
    global new_map, new_spot_map, new_spot_list, sr, sc, sd, ans
    fish_move()
    tmp_map = copy.deepcopy(new_map)
    tmp_spot_map = copy.deepcopy(new_spot_map)
    tmp_spot_list = copy.deepcopy(new_spot_list)
    tmp_tong = [sr,sc,sd]
    for i in range(1,4):
        nr = sr + dr[sd] * i
        nc = sc + dc[sd] * i
        if nr >= 4 or nr < 0 or nc >= 4 or nc < 0:
            ans = max(ans, food_cnt)
            return
        if new_map[nr][nc][0] == 0: continue
        new_map[sr][sc] = [0,0]
        sr, sc, sd = nr, nc, new_map[nr][nc][1]
        food = new_map[nr][nc][0]
        new_map[nr][nc] = [-1,-1]
        dfs(food_cnt + food)
        sr, sc, sd = tmp_tong
        new_map = copy.deepcopy(tmp_map)
        new_spot_list = copy.deepcopy(tmp_spot_list)
        new_spot_map = copy.deepcopy(tmp_spot_map)
    return


def fish_move():
    global new_spot_map,new_spot_list
    for i in range(1,17):
        r, c = new_spot_list[i]
        d = new_map[r][c][1]
        if new_map[r][c][0] < 1:
            continue
        for j in range(8):
            nd = (d + j) % 8
            nr = r + dr[nd]
            nc = c + dc[nd]
            if nr >= 4 or nr < 0 or nc >= 4 or nc < 0 or new_map[nr][nc][0] == -1: continue
            target = new_spot_map[nr][nc]
            new_map[r][c][1] = nd
            new_map[nr][nc], new_map[r][c] = new_map[r][c], new_map[nr][nc]
            new_spot_list[i], new_spot_list[target] = new_spot_list[target], new_spot_list[i]
            new_spot_map[r][c], new_spot_map[nr][nc] = new_spot_map[nr][nc], new_spot_map[r][c]
            break
    return


MAP = [[[0, 0] for _ in range(4)] for _ in range(4)]
# 물고기 위치
spot_list = [[0, 0] for _ in range(17)]
# 위치별 물고기 번호
spot_map = [[0] * 4 for _ in range(4)]
for f in range(4):
    tmp = list(map(int, input().split()))
    for t in range(8):
        if t % 2:
            MAP[f][t // 2][1] = tmp[t] - 1
        else:
            MAP[f][t // 2][0] = tmp[t]
            spot_list[tmp[t]] = [f, t // 2]
            spot_map[f][t // 2] = tmp[t]
ans = 0
# 먹힌 물고기는 [-1, -1] 처리
ans += MAP[0][0][0]
# 상어 위치 및 방향
sr, sc, sd = 0, 0, MAP[0][0][1]
# MAP에서 -1, -1은 상어를 의미
MAP[0][0] = [-1, -1]
new_map = copy.deepcopy(MAP)
new_spot_list = copy.deepcopy(spot_list)
new_spot_map = copy.deepcopy(spot_map)
dfs(ans)
print(ans)
