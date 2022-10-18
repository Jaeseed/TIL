def solution(str1, str2):
    list1 = []
    list2 = []
    same_cnt = 0
    for i1 in range(len(str1)-1):
        if 97 <= ord(str1[i1].lower()) <= 122 and 97 <= ord(str1[i1+1].lower()) <= 122:
            list1.append(str1[i1].lower() + str1[i1+1].lower())
    for i2 in range(len(str2)-1):
        if 97 <= ord(str2[i2].lower()) <= 122 and 97 <= ord(str2[i2+1].lower()) <= 122:
            list2.append(str2[i2].lower() + str2[i2+1].lower())
    visited = [0] * len(list2)
    for st1 in list1:
        for i2 in range(len(list2)):
            if visited[i2]: continue
            if st1 == list2[i2]:
                same_cnt += 1
                visited[i2] = 1
                break
    union_cnt = len(list1) + len(list2) - same_cnt
    if len(list1) == 0 and len(list2) == 0:
        answer = 65536
    elif same_cnt == 0:
        answer = 0
    else:
        answer = int(same_cnt / union_cnt * 65536)
    print(answer)
    return answer
solution('aa1+aa2', 'AAAA12')