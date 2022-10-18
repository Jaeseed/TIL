def compare(str1, str2):
    if len(str1) != len(str2):
        return False
    for i in range(len(str1)):
        dif = ord(str1[i]) - ord(str2[i])
        if abs(dif) == 0 or abs(dif) == 32:
            continue
        return False
    return True

def solution(cacheSize, cities):
    answer = 0
    cache_list = []
    head = 0
    tail = 0
    for city in cities:
        idx = head
        flag = 0
        while idx < tail:
            if compare(cache_list[idx], city):
                flag = 1
                cache_list.pop(idx)
                answer += 1
                break
            idx += 1
        cache_list.append(city)
        if flag == 0:
            answer += 5
            if tail - head < cacheSize:
                tail += 1
            else:
                tail += 1
                head += 1
    return answer