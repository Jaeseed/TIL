def make_answer(order):
    global max_value, min_value
    answer = num_list[0]
    idx = 1
    for o in order:
        if o == '0':
            answer += num_list[idx]
        elif o == '1':
            answer -= num_list[idx]
        elif o == '2':
            answer *= num_list[idx]
        else:
            if answer < 0:
                answer = (abs(answer) // num_list[idx]) * -1
            else:
                answer //= num_list[idx]
        idx += 1
    max_value = max(max_value, answer)
    min_value = min(min_value, answer)


def dfs(step, order):
    if step == N-1:
        make_answer(order)
        return
    for i in range(4):
        if calculator[i] == 0:
            continue
        calculator[i] -= 1
        dfs(step+1, order + str(i))
        calculator[i] += 1

    return


N = int(input())
num_list = list(map(int, input().split()))
calculator = list(map(int, input().split()))
max_value = -2e29
min_value = 2e29
dfs(0, '')
print(max_value)
print(min_value)