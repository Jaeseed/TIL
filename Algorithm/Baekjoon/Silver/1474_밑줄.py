N, M = map(int,input().split())
word_list = []
first_length = 0
for n in range(N):
    now_word = input()
    word_list.append(now_word)
    first_length += len(now_word)
under_bar_cnt = M - first_length
average_under_bar = under_bar_cnt // (N-1)
pass_cnt = N-1 - under_bar_cnt % (N-1)
new_word = word_list[0]
for i in range(1, N):
    unit = word_list[i]
    if pass_cnt >= N - i:
        pass
    elif unit[0].isupper() and pass_cnt:
        pass_cnt -= 1
    else:
        new_word += '_'
    new_word += '_' * average_under_bar + unit
print(new_word)
