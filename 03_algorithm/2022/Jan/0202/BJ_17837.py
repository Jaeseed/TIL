import sys
dr = [0,0,-1,1]
dc = [1,-1,0,0]
change_direction = [1,0,3,2]


def ans_check():
    for r in range(N):
        for c in range(N):
            if len(unit_map[r][c]) >= 4:
                return True
    return False


N, K = map(int, input().split())
MAP = [list(map(int,input().split())) for _ in range(N)]
unit_map = [[[] for Q in range(N)] for _ in range(N)]
unit_location_list = [0] * (K+1)
for k in range(K):
    row,col,d = map(int,sys.stdin.readline().split())
    if unit_map[row-1][col-1] == [0]:
        unit_map[row-1][col-1] = [k+1]
    else:
        unit_map[row-1][col-1].append(k+1)
    unit_location_list[k+1] = [row-1,col-1,d-1]
turn = 0
flag = 0
while turn < 1000 and flag == 0:
    turn += 1
    for k in range(1,K+1):
        row, col, d = unit_location_list[k]
        for i in range(len(unit_map[row][col])):
            if unit_map[row][col][i] == k:
                break
        tmp = unit_map[row][col][i:]
        nr, nc = row + dr[d], col + dc[d]
        if nr >= N or nr < 0 or nc >= N or nc < 0 or MAP[nr][nc] == 2:
            d = change_direction[d]
            unit_location_list[k][2] = d
            nr, nc = row + dr[d], col + dc[d]
            if nr >= N or nr < 0 or nc >= N or nc < 0 or MAP[nr][nc] == 2: continue
        if MAP[nr][nc] == 0:
            unit_map[row][col] = unit_map[row][col][:i]
            unit_map[nr][nc] += tmp
            for t in tmp:
                unit_location_list[t][0], unit_location_list[t][1] = nr, nc
        else:
            tmp.reverse()
            unit_map[row][col] = unit_map[row][col][:i]
            unit_map[nr][nc] += tmp
            for t in tmp:
                unit_location_list[t][0], unit_location_list[t][1] = nr, nc
        if len(unit_map[nr][nc]) >= 4:
            flag = 1
            break
if flag == 0:
    turn = -1
print(turn)

