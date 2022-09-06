word = input()
absolute_cnt = 0
cnt = 0
alphabet = ['w', 'o', 'l', 'f']
alphabet_idx = 0
flag = 1
for w in word:
    before = alphabet[alphabet_idx]
    if w == before:
        cnt += 1
    else:
        if w != alphabet[(alphabet_idx + 1) % 4]:
            flag = 0
            break
        if before == 'w':
            absolute_cnt = cnt
        else:
            if cnt != absolute_cnt:
                flag = 0
                break
            if before == 'f':
                alphabet_idx = -1
        cnt = 1
        alphabet_idx += 1
if flag == 0:
    print(0)
else:
    if alphabet[alphabet_idx] == 'f' and absolute_cnt == cnt:
        print(1)
    else:
        print(0)

