def pop_left(front, rear, gem_idx_dict, gems):
    for s in range(front, rear):
        front_gem = gems[s]
        if gem_idx_dict[front_gem] == s:
            return s
    return front


def solution(gems):
    gems_set = set(gems)
    gem_idx_dict = dict()
    tmp = 0
    for key in gems_set:
        gem_idx_dict[key] = -1
        tmp += 1
    total_gems_cnt = len(gem_idx_dict)
    cnt_at_this_time = 0
    idx = 0
    # 모든 보석을 다 담을 때까지 while문 반복
    while cnt_at_this_time < total_gems_cnt:
        now_gem = gems[idx]
        if gem_idx_dict[now_gem] == -1:
            cnt_at_this_time += 1
        gem_idx_dict[now_gem] = idx
        idx += 1
    front = 0
    rear = idx - 1
    front = pop_left(front, rear, gem_idx_dict, gems)
    answer = [front,rear]
    for s in range(rear+1, len(gems)):
        now_gem = gems[s]
        gem_idx_dict[now_gem] = s
        front = pop_left(front, s, gem_idx_dict, gems)
        if s - front < answer[1] - answer[0]:
            answer = [front, s]
    print(answer)
    answer[0] += 1
    answer[1] += 1
    return answer


solution(	["AA", "AB", "AC", "AA", "AC"])
