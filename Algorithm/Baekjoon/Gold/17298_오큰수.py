N = int(input())
numbers = list(map(int,input().split()))
stack = []
num_info = []
answer = [0] * N
for i in range(N):
    num_info.append([numbers[i], i])
for i in range(N):
    now = num_info[i]
    if not stack:
        stack.append(now)
    else:
        if stack[-1][0] < now[0]:
            while stack and stack[-1][0] < now[0]:
                pop_num = stack.pop()
                answer[pop_num[1]] = now[0]
        stack.append(now)
for st in stack:
    answer[st[1]] = -1
print(' '.join(map(str,answer)))