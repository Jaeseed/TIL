dr = [0,0,0,-1,1]
dc = [0,1,-1,0,0]

N, M, x, y, K = map(int,input().split())
MAP = [list(map(int,input().split())) for _ in range(N)]
order = list(map(int,input().split()))
dice = [0] * 6
for k in range(K):
    direction = order[k]
    nx = x + dr[direction]
    ny = y + dc[direction]
    if nx >= N or nx < 0 or ny >= M or ny < 0: continue
    y = ny
    x = nx
    tong = dice[:]
    if direction == 1:
        tmp = dice[0]
        tong[0] = dice[1]
        tong[5] = dice[2]
        tong[1] = dice[5]
        tong[2] = tmp
    elif direction == 2:
        tmp = dice[0]
        tong[0] = dice[2]
        tong[5] = dice[1]
        tong[2] = dice[5]
        tong[1] = tmp
    elif direction == 3:
        tmp = dice[0]
        tong[0] = dice[3]
        tong[5] = dice[4]
        tong[3] = dice[5]
        tong[4] = tmp
    else:
        tmp = dice[0]
        tong[5] = dice[3]
        tong[0] = dice[4]
        tong[4] = dice[5]
        tong[3] = tmp
    dice = tong[:]
    if MAP[x][y] == 0:
        MAP[x][y] = dice[0]
    else:
        dice[0] = MAP[x][y]
        MAP[x][y] = 0
    print(dice[5])
