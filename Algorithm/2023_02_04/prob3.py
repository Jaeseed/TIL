from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(ro, co, color, MAP, visited):
    qu = deque()
    # 모든 인접 마카롱 row, column 저장
    route = [[ro, co]]
    qu.append([ro, co])
    while qu:
        r, c = qu.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 맵 외부로 나가는 것 방지 / visited와 색깔 체크
            if nr >= 6 or nr < 0 or nc >= 6 or nc < 0 or visited[nr][nc] or MAP[nr][nc] != color:
                continue
            visited[nr][nc] = 1
            qu.append([nr, nc])
            route.append([nr, nc])
    return route


def bomb(target_list, MAP):
    for target in target_list:
        ro, co = target
        MAP[ro][co] = 0
    return


def gravity(MAP):
    for co in range(6):
        jump = 0
        for ro in range(5,-1,-1):
            if MAP[ro][co] == 0:
                jump += 1
            else:
                # 빈칸에 마카롱 교체
                MAP[ro + jump][co], MAP[ro][co] = MAP[ro][co], MAP[ro + jump][co]
    return


def solution(macaron):
    answer = []
    # 마카롱 전체 맵
    MAP = [[0] * 6 for _ in range(6)]
    for column, color in macaron:
        column, color = int(column), int(color)
        column -= 1
        # 마카롱 떨어트리기
        for row in range(5, -1, -1):
            if MAP[row][column]:
                continue
            MAP[row][column] = color
            break
        # 인접 마카롱 체크
        visited = [[0] * 6 for _ in range(6)]
        visited[row][column] = 1
        # 인접 마카롱의 row, column 값
        adj = bfs(row, column, color, MAP, visited)
        # 3개 이상일 때 터트리고 정렬
        if len(adj) >= 3:
            bomb(adj, MAP)
            gravity(MAP)
            # 터진 후 3개 이상 붙은 마카롱 탐색
            while True:
                n_visited = [[0] * 6 for _ in range(6)]
                tong = []
                for r in range(6):
                    for c in range(6):
                        if MAP[r][c] and n_visited[r][c] == 0:
                            # new visited
                            n_visited[r][c] = 1
                            # 인접 마카롱의 row, column 값
                            n_adj = bfs(r, c, MAP[r][c], MAP, n_visited)
                            # 인접 마카롱 3개 이상일 때 삭제 목록에 추가
                            if len(n_adj) >= 3:
                                tong += n_adj
                # 터트릴 마카롱이 없을 때 break
                if not tong:
                    break
                bomb(tong, MAP)
                gravity(MAP)
    for r in range(6):
        answer.append(''.join(map(str,MAP[r])))
    return answer
solution(
[[1, 1], [1, 2], [1, 4], [2, 1], [2, 2], [2, 3], [3, 4], [3, 1], [3, 2], [3, 3], [3, 4], [4, 4], [4, 3], [5, 4], [6, 1]])