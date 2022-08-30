N = int(input())
soldier_strength = list(map(int,input().split()))
dp = [1] * N
for i in range(1, N):
    max_value_before = 0
    for j in range(i):
        if soldier_strength[j] > soldier_strength[i] and dp[j] > max_value_before:
            max_value_before = dp[j]
    dp[i] = max_value_before + 1
print(N - max(dp))
