import sys
N = int(input())
progression = [int(sys.stdin.readline()) for _ in range(N)]
stack = []
idx = 0
answer = []
for i in range(1, N+1):
    stack.append(i)
    answer.append('+')
    if i == progression[idx]:
        while idx < N and stack and progression[idx] == stack[-1]:
            stack.pop()
            answer.append('-')
            idx += 1
if stack:
    print('NO')
else:
    for a in answer:
        print(a)