# # 풀이1. 완전탐색
# def greeting(idx, fatigue, happiness):
#     global answer
#     for i in range(idx, N):
#         if fatigue_list[i] + fatigue < 100:
#             greeting(i + 1, fatigue_list[i] + fatigue, happiness + happiness_list[i])
#     answer = max(answer, happiness)
#     return
#
#
# N = int(input())
# # 피로도 리스트
# fatigue_list = list(map(int, input().split()))
# # 행복도 리스트
# happiness_list = list(map(int, input().split()))
# answer = 0
# greeting(0, 0, 0)
# print(answer)

# 풀이2. DP
N = int(input())
# 피로도 리스트
fatigue_list = [0] + list(map(int, input().split()))
# 행복도 리스트
happiness_list = [0] + list(map(int, input().split()))
DP = [[0] * 101 for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, 101):
        if fatigue_list[i] >= j:
            DP[i][j] = DP[i-1][j]
        else:
            DP[i][j] = max(DP[i-1][j], DP[i-1][j-fatigue_list[i]] + happiness_list[i])
    answer = max(DP[i])
print(answer)