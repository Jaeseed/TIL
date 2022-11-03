from collections import deque
import copy

dr = [0, -1, 0]
dc = [-1, 0, 1]


def choose_row(idx, idx_list):
    if len(idx_list) == 3:
        defense(idx_list)
        return
    for i in range(idx + 1, M):
        choose_row(i, idx_list + [i])
    return


def defense(archer_list):
    global answer
    cnt = 0
    # 3개의 장소를 임의로 정할 때마다 쓰는 간이용 맵
    now_map = copy.deepcopy(MAP)
    # 시작 행
    sr = N - 1
    # visited를 숫자로 관리하여 계속 생성 안 하게 만듬
    visited_num = 1
    visited = [[0] * M for _ in range(N)]
    # 모든 행 다 돌 때까지
    while sr >= 0:
        # 세 자리에서의 목표물 리스트
        target = []
        for i in range(3):
            if now_map[sr][archer_list[i]]:
                target.append([sr,archer_list[i]])
                continue
            if D == 1:
                continue
            qu = deque()
            qu.append([sr, archer_list[i], 1])
            visited[sr][archer_list[i]] = visited_num
            while qu:
                r, c, d = qu.popleft()
                for j in range(3):
                    nr = r + dr[j]
                    nc = c + dc[j]
                    if nr < 0 or nc >= M or nc < 0 or visited[nr][nc] == visited_num: continue
                    # 적이 있을 시에 break
                    if now_map[nr][nc]:
                        target.append([nr, nc])
                        qu = []
                        break
                    # 거리가 D와 같을 땐 qu에 갱신 X
                    if d == D-1:
                        continue
                    qu.append([nr, nc, d + 1])
                    visited[nr][nc] = visited_num
            visited_num += 1
        for enemy_r, enemy_c in target:
            if now_map[enemy_r][enemy_c]:
                now_map[enemy_r][enemy_c] = 0
                cnt += 1
        sr -= 1
    answer = max(answer, cnt)
    return


N, M, D = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
answer = 0
# 3개의 자리를 재귀함수로 모두 방문
choose_row(-1, [])
print(answer)