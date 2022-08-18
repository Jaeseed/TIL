# idx 1부터 순서대로 동, 서, 북, 남
dr = [0,0,0,-1,1]
dc = [0,1,-1,0,0]

N, M, r, c, K = map(int,input().split())
MAP = [list(map(int,input().split())) for _ in range(N)]
order_list = list(map(int,input().split()))

# 주사위의 각 면 / 순서대로 위, 뒤, 우, 좌, 앞, 아래
dice = [0,0,0,0,0,0]

for order in order_list:
    nr = r + dr[order]
    nc = c + dc[order]
    # 리스트 밖으로 나가는 상황 거르기
    if nr >= N or nr < 0 or nc >= M or nc < 0: continue
    # 거르기 통과 시 r, c 재할당
    r, c = nr, nc
    # 동
    if order == 1:
        tmp = dice[0]
        dice[0] = dice[3]
        dice[3] = dice[5]
        dice[5] = dice[2]
        dice[2] = tmp
    # 서
    elif order == 2:
        tmp = dice[0]
        dice[0] = dice[2]
        dice[2] = dice[5]
        dice[5] = dice[3]
        dice[3] = tmp
    # 북
    elif order == 3:
        tmp = dice[0]
        dice[0] = dice[4]
        dice[4] = dice[5]
        dice[5] = dice[1]
        dice[1] = tmp
    # 남
    elif order == 4:
        tmp = dice[0]
        dice[0] = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[4]
        dice[4] = tmp
    # 칸이 0일 때 칸의 숫자를 주사위 바닥면으로 갱신
    if MAP[nr][nc] == 0:
        MAP[nr][nc] = dice[5]
    # 칸이 0이 아닐 때 주사위 바닥면 갱신 및 칸 0으로 초기화
    else:
        dice[5] = MAP[nr][nc]
        MAP[nr][nc] = 0
    print(dice[0])
