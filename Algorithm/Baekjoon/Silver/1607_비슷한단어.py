def words_check(w1, w2):
    yellow_card = 0
    value = 0
    for i in range(26):
        if w1[i] != w2[i]:
            if abs(w1[i] - w2[i]) > 1:
                return 0
            elif yellow_card == 0:
                value = w1[i] - w2[i]
            elif yellow_card == 1:
                if w1[i] - w2[i] + value != 0:
                    return 0
            else:
                return 0
            yellow_card += 1
    return 1


N = int(input())
words = [[0] * 26 for _ in range(N)]
for n in range(N):
    now = input()
    for no in now:
        idx = ord(no) - ord('A')
        words[n][idx] += 1
answer = 0
for n in range(1, N):
    answer += words_check(words[0], words[n])
print(answer)