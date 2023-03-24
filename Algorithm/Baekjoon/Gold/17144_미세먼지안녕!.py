dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def diffusion():
    global MAP
    tong = [[0] * M for _ in range(N)]
    for n in range(N):
        for m in range(M):
            if MAP[n][m] <= 0: continue
            now = MAP[n][m]
            delta = now // 5
            cnt = 0
            for i in range(4):
                nn = n + dr[i]
                nm = m + dc[i]
                if nn >= N or nn < 0 or nm >= M or nm < 0 or MAP[nn][nm] == -1: continue
                tong[nn][nm] += delta
                cnt += 1
            MAP[n][m] -= delta * cnt
    for n in range(N):
        for m in range(M):
            MAP[n][m] += tong[n][m]
    return


def move():
    # 위 공기 순환
    tr, tc = machine[0]-1 , 0
    td = 0
    MAP[tr][tc] = 0
    while True:
        ntr = tr + dr[td]
        ntc = tc + dc[td]
        if ntr > machine[0] or ntr < 0 or ntc >= M or ntc < 0:
            td += 1
            continue
        if ntr == machine[0] and ntc == 0:
            MAP[tr][tc] = 0
            break
        MAP[tr][tc] = MAP[ntr][ntc]
        tr,tc = ntr, ntc

    # 아래 공기 순환
    br, bc = machine[1]+1, 0
    bd = 3
    MAP[br][bc] = 0
    while True:
        nbr = br + dr[bd]
        nbc = bc + dc[bd]
        if nbr < machine[1] or nbr >= N or nbc >= M or nbc < 0:
            bd -= 1
            continue
        if nbr == machine[1] and nbc == 0:
            MAP[br][bc] = 0
            break
        MAP[br][bc] = MAP[nbr][nbc]
        br,bc = nbr, nbc
    return


N, M, T = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
machine = []
for r in range(N):
    if MAP[r][0] == -1:
        machine.append(r)
time = 0
while T > time:
    diffusion()
    move()
    time += 1
answer = 0

for r in range(N):
    for c in range(M):
        if MAP[r][c] == -1: continue
        answer += MAP[r][c]
print(answer)