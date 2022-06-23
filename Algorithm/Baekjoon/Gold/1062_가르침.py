def choose_words(used_alpha, used_word, idx):
    if idx == N:
        choose_alphabet(used_alpha, used_word)
        return
    for i in range(idx, N):
        candidate_used_alpha = used_alpha | words[i]
        if len(candidate_used_alpha) > K:
            continue
        choose_words(candidate_used_alpha, used_word +[i], i + 1)
    choose_alphabet(candidate_used_alpha, used_word)
    return


def choose_alphabet(used_alpha, used_word):
    global not_used_alpha, not_used_word, new_K
    not_used_word = []
    not_used_alpha = []
    used_alpha = list(used_alpha)
    for i in range(N):
        if i not in used_word:
            not_used_word.append(i)
    for u in all_alpha:
        if u in used_alpha:
            continue
        not_used_alpha.append(u)
    dfs(0, 0, '')
    return


def dfs(step, idx, chosen_alpha):
    if step == new_K:
        calculate(chosen_alpha)
        return
    for i in range(idx, len(not_used_alpha)):
        dfs(step + 1, idx + 1, chosen_alpha + not_used_alpha[i])
    return


def calculate(chosen_alpha):
    global answer
    cnt = N - len(not_used_word)
    final_alpha = []
    for m in not_used_alpha:
        if m in chosen_alpha:
            continue
        final_alpha.append(m)
    for idx in not_used_word:
        flag = 1
        for alpha in words[idx]:
            if alpha not in final_alpha:
                flag = 0
                break
        if flag == 1:
            cnt += 1
    answer = max(answer, cnt)
    return


N, K = map(int, input().split())
words = []
all_alpha = set()
for n in range(N):
    input_word = set(list(input()))
    words.append(input_word)
    all_alpha |= input_word
new_K = 0
not_used_word = []
not_used_alpha = []
answer = 0
choose_words(set(), [], 0)
print(answer)