def calculation(idx, past):
    global flag, visited
    # 현재 총 값
    total = 0
    for i in range(idx, len(problem)):
        # 방문 체크
        if visited[i] == 1: continue
        # 방문 갱신
        visited[i] = 1
        if flag == 0:
            return 0
        if problem[i] == '(' or problem[i] == '[':
            total += calculation(i+1, problem[i])
        else:
            # 재귀함수의 가장 바깥이거나 괄호가 안 맞으면 괄호 비성사
            if not past or bracket_dict[past] != bracket_dict[problem[i]]:
                flag = 0
                return 0
            # 곱하기 시 0 되는 경우 방지
            if total == 0:
                total = 1
            total *= bracket_dict[past]
            return total
    # 괄호가 안 닫힌 경우 체크
    if past:
        flag = 0
        return 0
    return total


problem = input()
# 괄호의 값
bracket_dict = {'(': 2, ')': 2, '[': 3, ']': 3}
visited = [0] * len(problem)
# 괄호 성사 여부 판단 변수
flag = 1
# 괄호 성사 안 될 시 0 출력
if problem[0] == ')' or problem[0] == ']':
    print(0)
else:
    answer = calculation(0, '')
    if flag == 0:
        print(0)
    else:
        print(answer)