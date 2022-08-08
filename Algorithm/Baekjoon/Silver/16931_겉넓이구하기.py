# 1. MAP을 architecture로 옮겨 전체 탐색
# # 위,아래,상,하,좌,우 탐색
# dh = [-1, 1, 0, 0, 0, 0]
# dn = [0, 0, -1, 1, 0, 0]
# dm = [0, 0, 0, 0, -1, 1]
#
# # 가로 세로 길이 입력
# N, M = map(int, input().split())
# # H 변수 선언
# H = 0
# # 박스 배치 입력값 받기
# MAP = []
# for n in range(N):
#     tmp = list(map(int, input().split()))
#     # 박스의 최대 높이 구하기
#     tmp_H = max(tmp)
#     H = max(H, tmp_H)
#     MAP.append(tmp)
# # 3차원 리스트 / 전체 설계도 (순서 H -> N -> M)
# architecture = [[[0] * M for _ in range(N)] for _ in range(H)]
# # 설계도에 값 채우기
# for h in range(H):
#     for n in range(N):
#         for m in range(M):
#             if MAP[n][m] > 0:
#                 architecture[h][n][m] += 1
#                 MAP[n][m] -= 1
# answer = 0
# # 전체 탐색
# for h in range(H):
#     for n in range(N):
#         for m in range(M):
#             if architecture[h][n][m] == 0:
#                 continue
#             for i in range(6):
#                 # 6방향 인덱스 탐색
#                 nh = h + dh[i]
#                 nn = n + dn[i]
#                 nm = m + dm[i]
#                 if nh >= H or nh < 0 or nn >= N or nn < 0 or nm >= M or nm < 0:
#                     answer += 1
#                     continue
#                 if architecture[nh][nn][nm]:
#                     continue
#                 answer += 1
# print(answer)

# 2. MAP으로 바로 전체 탐색
# 2차원 델타 리스트
# dn = [-1,1,0,0]
# dm = [0,0,-1,1]
#
# N, M = map(int,input().split())
# MAP = [list(map(int,input().split())) for _ in range(N)]
# answer = 0
# H = 0
# for n in range(N):
#     for m in range(M):
#
#         if MAP[n][m]:
#             answer += 1
#             H = max(H, MAP[n][m])
# now_height = 0
# while now_height < H:
#     for n in range(N):
#         for m in range(M):
#             if MAP[n][m] == 0:
#                 continue
#             for i in range(4):
#                 nn = n + dn[i]
#                 nm = m + dm[i]
#                 if nn >= N or nn < 0 or nm >= M or nm < 0:
#                     answer += 1
#                     continue
#                 if MAP[nn][nm] == 0:
#                     answer += 1
#     for n in range(N):
#         for m in range(M):
#             if MAP[n][m] >= 1:
#                 if MAP[n][m] == 1:
#                     answer += 1
#                 MAP[n][m] -= 1
#     now_height += 1
# print(answer)
#

# 3. MAP의 높이별 차이 계산을 통한 풀이
N,M = map(int,input().split())
MAP = [list(map(int,input().split())) for _ in range(N)]
answer = 0
# 1) 윗면 아랫면 계산
for n in range(N):
    for m in range(M):
        if MAP[n][m]:
            answer += 2
# 2) 좌우면
# 2-1) 각 m의 위치마다 넓이 계산
for n in range(N):
    for m in range(M-1):
        left = MAP[n][m] - MAP[n][m + 1]
        right = MAP[n][m + 1] - MAP[n][m]
        if left > 0:
            answer += left
        if right > 0:
            answer += right
# 2-2) 양쪽 끝면 계산
for n in range(N):
    for m in range(-1,1):
        answer += MAP[n][m]
# 3) 앞뒤면
# 3-1) 각 n 위치마다 넓이 계산
for m in range(M):
    for n in range(N-1):
        front = MAP[n+1][m] - MAP[n][m]
        back = MAP[n][m] - MAP[n+1][m]
        if front > 0:
            answer += front
        if back > 0:
            answer += back
# 3-2) 얖쪽 끝면 계산
for m in range(M):
    for n in range(-1,1):
        answer += MAP[n][m]
print(answer)