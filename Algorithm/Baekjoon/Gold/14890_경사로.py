N, L = map(int,input().split())
MAP = [list(map(int,input().split())) for _ in range(N)]
answer = 0

# 1. 가로 길
for r in range(N):
    c = 1
    # 해당 길의 가능 유무
    flag = 1
    # 해당 칸의 경사로 유무
    visited = [0] * N
    while c < N:
        # 이전 칸의 높이
        before = MAP[r][c-1]
        # 높이 차 2칸 이상 제외
        if abs(before - MAP[r][c]) > 1:
            flag = 0
            break
        # 한 칸 낮은 경우
        elif before - MAP[r][c] == 1:
            # 현재 길이
            l = 1
            # 탐색할 열 값
            nc = c
            visited[nc] = 1
            now = MAP[r][c]
            while l < L:
                nc += 1
                if nc >= N or MAP[r][nc] != now or visited[nc] == 1:
                    flag = 0
                    break
                visited[nc] = 1
                l += 1
            if flag == 1:
                c = nc
        # 한 칸 높은 경우
        elif before - MAP[r][c] == -1:
            # 현재 길이
            l = 1
            # 탐색할 열 값
            nc = c - 1
            if visited[nc] == 1:
                flag = 0
                break
            now = MAP[r][c-1]
            while l < L:
                nc -= 1
                if nc < 0 or MAP[r][nc] != now or visited[nc] == 1:
                    flag = 0
                    break
                l += 1
        # 가능 여부 체크
        if flag == 0:
            break
        c += 1
    if flag == 1:
        answer += 1

# 2. 세로 길
for c in range(N):
    r = 1
    # 해당 길의 가능 유무
    flag = 1
    # 해당칸의 경사로 유무
    visited = [0] * N
    while r < N:
        # 이전 칸의 높이
        before = MAP[r-1][c]
        # 높이 차 2칸 이상 제외
        if abs(before - MAP[r][c]) > 1:
            flag = 0
            break
        # 한 칸 낮은 길
        elif before - MAP[r][c] == 1:
            # 현재 길이
            l = 1
            # 탐색할 행 값
            nr = r
            visited[nr] = 1
            now = MAP[r][c]
            while l < L:
                nr += 1
                if nr >= N or MAP[nr][c] != now or visited[nr] == 1:
                    flag = 0
                    break
                visited[nr] = 1
                l += 1
            if flag == 1:
                r = nr
        # 한 칸 높은 길
        elif before - MAP[r][c] == -1:
            # 현재 길이
            l = 1
            # 탐색할 행 값
            nr = r - 1
            if visited[nr] == 1:
                flag = 0
                break
            now = MAP[r-1][c]
            while l < L:
                nr -= 1
                if nr < 0 or MAP[nr][c] != now or visited[nr] == 1:
                    flag = 0
                    break
                l += 1
        # 성사여부 체크
        if flag == 0:
            break
        r += 1
    if flag == 1:
        answer += 1
print(answer)