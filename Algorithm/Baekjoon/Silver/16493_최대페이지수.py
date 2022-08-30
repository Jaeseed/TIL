N, M = map(int,input().split())

input_list = [[0,0]] + [list(map(int,input().split())) for _ in range(M)]
dp = [[0] * (N + 1) for _ in range(M+1)]
answer = 0
for i in range(1, M+1):
    for j in range(1, N+1):
        if j >= input_list[i][0]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-input_list[i][0]] + input_list[i][1])
        else:
            dp[i][j] = dp[i-1][j]
    answer = max(max(dp[i]), answer)
print(answer)