import sys
dr = [-1,1,0,0]
dc = [0,0,1,-1]


def shark_move():
    global MAP
    shark_tong = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if MAP[r][c]:
                v, di, size = MAP[r][c]
                MAP[r][c] = 0
                nr, nc = r, c
                nv = v
                while nv > 0:
                    if nr + dr[di] >= R or nr + dr[di] < 0 or nc + dc[di] >= C or nc + dc[di] < 0:
                        if di % 2:
                            di -= 1
                        else:
                            di += 1
                    nr += dr[di]
                    nc += dc[di]
                    nv -= 1
                if shark_tong[nr][nc]:
                    if shark_tong[nr][nc][2] > size:
                        continue
                shark_tong[nr][nc] = (v,di,size)
    MAP = [shark_tong[_][:] for _ in range(R)]
    return


R, C, M = map(int,input().split())
MAP = [[0] * C for _ in range(R)]
fishing_total = 0
for m in range(M):
    r_, c_, s_, d_, z_ = map(int,sys.stdin.readline().split())
    d_ -= 1
    MAP[r_-1][c_-1] = (s_,d_,z_)
for col in range(C):
    row = 0
    while row < R:
        if MAP[row][col]:
            fishing_total += MAP[row][col][2]
            MAP[row][col] = 0
            break
        row += 1
    shark_move()
print(fishing_total)
