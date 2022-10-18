# def solution(registered_list, new_id):
#     registered_list.sort()
#     S = ''
#     N_str = ''
#     for unit in new_id:
#         if 48 <= ord(unit) <= 57:
#             N_str += unit
#         else:
#             S += unit
#     # N 값이 null인 상황 체크
#     if S == new_id:
#         N_str = '0'
#     N_num = int(N_str)
#     # 기존에 있는 아이디일 때
#     if new_id in registered_list:
#         start = registered_list.index(new_id)
#         # 아이디 추천 완료 체크
#         complete_check = 0
#         for idx in range(start+1, len(registered_list)):
#             N_num += 1
#             new_id = S + str(N_num)
#             if new_id != registered_list[idx]:
#                 complete_check = 1
#                 break
#         if complete_check == 0:
#             N_num += 1
#             new_id = S + str(N_num)
#     # 기존에 없는 아이디일 때
#     else:
#         if N_num != 0:
#             new_id = S + str(N_num)
#         else:
#             new_id = S
#     answer = new_id
#     print(answer)
#     return answer
# solution(
# ["cow", "coww1", "cow2", "cow3", "cow4", "cow9", "cow8", "cow7", "cow6", "cow5"], "cow")


from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def solution(maps):
    answer = 0
    N = len(maps)
    M = len(maps[0])
    for n in range(N):
        maps[n] = list(maps[n])
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if maps[i][j] != '.' and visited[i][j] == 0:
                qu = deque()
                qu.append([i, j])
                visited[i][j] = 1
                worlds = [[_, 0] for _ in range(26)]
                while qu:
                    r, c = qu.popleft()
                    world = maps[r][c]
                    worlds[ord(world) - 65][1] += 1
                    for n in range(4):
                        nr = r + dr[n]
                        nc = c + dc[n]
                        if nr >= N or nr < 0 or nc >= M or nc < 0 or visited[nr][nc] or maps[nr][nc] == '.':
                            continue
                        qu.append([nr, nc])
                        visited[nr][nc] = 1
                worlds.sort(key=lambda x: (x[1], x[0]))
                winners = [chr(worlds[-1][0] + 65)]

                for idx in range(25, -1,-1):
                    if worlds[idx][1] != worlds[-1][1]:
                        break
                    winners.append(chr(worlds[idx][0] + 65))
                qu = deque()
                qu.append([i, j])
                occupied = [[0] * M for _ in range(N)]
                while qu:
                    r, c = qu.popleft()
                    for n in range(4):
                        nr = r + dr[n]
                        nc = c + dc[n]
                        if nr >= N or nr < 0 or nc >= M or nc < 0 or occupied[nr][nc] or maps[nr][nc] == '.':
                            continue
                        if maps[nr][nc] not in winners:
                            maps[nr][nc] = winners[0]
                        qu.append([nr, nc])
                        occupied[nr][nc] = 1
    worlds_cnt = [0] * 26
    for r in range(N):
        for c in range(M):
            if maps[r][c] != '.':
                worlds_cnt[ord(maps[r][c]) - 65] += 1
    answer = max(worlds_cnt)
    return answer
solution(["XY..", "YX..", "..YX", ".AXY"])