first_word = input()
second_word = input()
f_len = len(first_word)
s_len = len(second_word)
dp = [[0] * (s_len + 1) for _ in range(f_len+1)]
answer = 0
for i in range(1,f_len+1):
    max_cnt = 0
    for j in range(1, s_len + 1):
        if first_word[i-1] == second_word[j-1]:
            dp[i][j] = max(dp[i-1][j-1] + 1, max_cnt)
            max_cnt = dp[i][j]
            answer = max(answer,max_cnt)
        else:
            dp[i][j] = max(dp[i-1][j], max_cnt)
print(answer)