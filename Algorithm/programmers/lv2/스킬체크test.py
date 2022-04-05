# 1
# def solution(skill, skill_trees):
#     answer = 0
#     for skill_tree in skill_trees:
#         skill_idx = 0
#         flag = 1
#         for unit in skill_tree:
#             if unit in skill:
#                 if skill[skill_idx] == unit:
#                     skill_idx += 1
#                 else:
#                     flag = 0
#                     break
#         if flag == 1:
#             answer += 1
#     return answer


# 2
def solution(number, k):
    answer = ''
    number = list(map(int,number))
    tong = [[number[0],0]]
    delete_idx = []
    idx = 1
    while k > 0:
        for i in range(len(tong)-1,-1,-1):
            if number[idx] <= tong[i][0]:
                break
            delete_idx.append(tong[i][1])
            k -= 1
            tong.pop()
            if k == 0:
                break
        tong.append([number[idx], idx])
        tong.sort(reverse=True)
        idx += 1
    for i in range(len(number)):
        if i in delete_idx:
            continue
        answer += str(number[i])
    return answer

solution("4177252841",4)