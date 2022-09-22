first_word = input()
second_word = input()
dp = [[0] * (len(second_word) + 1) for _ in range(len(first_word)+1)]
answer = 0
for i in range(1,len(first_word)+1):
    for j in range(1,len(second_word)+1):
        if first_word[i-1] == second_word[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            answer = max(answer, dp[i][j])
print(answer)