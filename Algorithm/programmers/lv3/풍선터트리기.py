def solution(a):
    answer = 0
    new_list = []
    for idx, value in enumerate(a):
        new_list.append([value, idx])
    new_list.sort()
    min_idx = new_list[0][1]
    max_idx = new_list[0][1]
    for value, idx in new_list:
        if min_idx < idx < max_idx:
            continue
        min_idx = min(min_idx, idx)
        max_idx = max(max_idx, idx)
        answer += 1
    return answer