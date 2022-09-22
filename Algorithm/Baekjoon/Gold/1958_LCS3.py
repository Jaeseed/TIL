first_word = input()
second_word = input()
third_word = input()
f_len, s_len, t_len = len(first_word), len(second_word), len(third_word)
answer = 0
dp = [[[0] * (t_len+1) for _ in range(s_len+1)] for i in range(f_len+1)]
for i in range(1, f_len+1):
    for j in range(1,s_len+1):
        max_cnt = 0
        for k in range(1,t_len+1):
            if first_word[i-1] == second_word[j-1] == third_word[k-1]:
                dp[i][j][k] = max(dp[i-1][j-1][k-1]+1, dp[i][j-1][k-1], max_cnt)
                answer = max(answer, dp[i][j][k])
                max_cnt = dp[i][j][k]
            else:
                dp[i][j][k] = max(dp[i-1][j][k], max_cnt)
print(answer)