def sorted_print(s, e):
    global answer_list
    if s == e:
        return
    min_value = 150
    min_idx = 0
    for i in range(s, e):
        if ascii_list[i] < min_value:
            min_value = ascii_list[i]
            min_idx = i
    make_word(min_idx)
    sorted_print(min_idx + 1, e)
    sorted_print(s, min_idx)
    return


def make_word(min_idx):
    global answer_list, visited
    visited[min_idx] = 1
    answer_list.append(min_idx)
    tmp = sorted(answer_list)
    answer = ''
    for t in tmp:
        answer += word[t]
    print(answer)
    return


word = input()
ascii_list = []
for w in range(len(word)):
    ascii_list.append(ord(word[w]))
answer_list = []
visited = [0] * len(word)
sorted_print(0, len(word))
