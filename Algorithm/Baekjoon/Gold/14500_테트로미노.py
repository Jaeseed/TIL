from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]


def bfs(ro, co):
    global answer
    qu = deque()
    qu.append([ro, co, 0, 0, -1])
    while qu:
        r, c, value, step, ban = qu.popleft()
        for i in range(4):
            if i == ban: continue
            nr = r + dr[i]
            nc = c + dc[i]
            if nr >= N or nr < 0 or nc >= M or nc < 0: continue
            if step == 3:
                answer = max(answer, value + MAP[nr][nc])
                continue
            qu.append([nr, nc, value + MAP[nr][nc], step + 1, (i + 2) % 4])
    return


def cross(ro, co):
    global answer
    tmp = MAP[ro][co]
    tong = []
    for i in range(4):
        nr = ro + dr[i]
        nc = co + dc[i]
        tong.append(MAP[nr][nc])
    tmp += sum(tong) - min(tong)
    answer = max(tmp, answer)
    return


N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
answer = 0
#1
for n in range(N):
    for m in range(M):
        bfs(n, m)
#2
for n in range(1, N - 1):
    for m in range(1, M - 1):
        cross(n, m)
print(answer)

# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]
# zi_first = [0, 1]
# zi_second = [[1,3],[0,2]]
#
# straight = [0,1,2]
#
# etc_first = [0,-1,-1,-1,0,1,1,1]
# etc_second = [-1,0,1,2,3,2,1,0]
#
#
# def zigzag(r, c):
#     global answer
#     for i in range(2):
#         for j in range(2):
#             value = MAP[r][c]
#             nr = r + dr[zi_first[i]]
#             nc = c + dc[zi_first[i]]
#             if nr >= N or nr < 0 or nc >= M or nc < 0: continue
#             value += MAP[nr][nc]
#             nr += dr[zi_second[i][j]]
#             nc += dc[zi_second[i][j]]
#             if nr >= N or nr < 0 or nc >= M or nc < 0: continue
#             value += MAP[nr][nc]
#             nr += dr[zi_first[i]]
#             nc += dc[zi_first[i]]
#             if nr >= N or nr < 0 or nc >= M or nc < 0: continue
#             value += MAP[nr][nc]
#             answer = max(answer, value)
#     return
#
#
# N, M = map(int, input().split())
# MAP = [list(map(int, input().split())) for _ in range(N)]
# answer = 0
#
# # 1. 정사각형
# for n in range(N - 1):
#     for m in range(M - 1):
#         tmp = MAP[n][m] + MAP[n + 1][m] + MAP[n][m + 1] + MAP[n + 1][m + 1]
#         answer = max(answer, tmp)
#
# # 2. 지그재그
# for n in range(N):
#     for m in range(M):
#         zigzag(n, m)
#
# # 3. 그 외 전부
# for n in range(N):
#     for m in range(M):
#         # 가로 3개 기준
#         now = 0
#         for st in straight:
#             if n + st >= N: break
#             now += MAP[n+st][m]
#         for etc in range(8):
#             nn = n + etc_second[etc]
#             nm = m + etc_first[etc]
#             if nn >= N or nn < 0 or nm >= M or nm < 0: continue
#             answer = max(answer, now + MAP[nn][nm])
#         # 세로 3개 기준
#         now = 0
#         for st in straight:
#             if m + st >= M: break
#             now += MAP[n][m+st]
#         for etc in range(8):
#             nn = n + etc_first[etc]
#             nm = m + etc_second[etc]
#             if nn >= N or nn < 0 or nm >= M or nm < 0: continue
#             answer = max(answer, now + MAP[nn][nm])
# print(answer)