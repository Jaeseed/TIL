## 2차원 dp
# N, K = map(int, input().split())
# things = []
# for n in range(N):
#     weight, value = map(int,input().split())
#     if value == 0:
#         continue
#     things.append([weight,value])
# new_length = len(things)
# dp = [[0] * (K+1) for _ in range(new_length+1)]
# for i in range(1, new_length+1):
#     w = things[i-1][0]
#     v = things[i-1][1]
#     for j in range(1, K+1):
#         if j >= w:
#             dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
#         else:
#             dp[i][j] = dp[i-1][j]
# print(dp[new_length][K])


## 1차원 dp
# 변수 받기
N, K = map(int,input().split())
# 물건 목록 리스트
things = []
for n in range(N):
    weight, value = map(int,input().split())
    # 가치 0이면 필요 없으니 버리기
    if value == 0:
        continue
    things.append([weight, value])
# 물건 목록 리스트 길이 구하기
new_length = len(things)
# dp 리스트 선언
dp = [0] * (K+1)
for i in range(new_length):
    # weight, value 받기
    w = things[i][0]
    v = things[i][1]
    # 뒤에서부터 오면서 가치 비교 및 수정
    for j in range(K, w-1, -1):
        if j >= w:
            dp[j] = max(dp[j], dp[j-w] + v)
print(dp[K])