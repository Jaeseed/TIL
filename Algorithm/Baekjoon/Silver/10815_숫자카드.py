N = int(input())
list_N = [0] * 20000001
tong = list(map(int,input().split()))
for t in range(N):
    list_N[tong[t]] = 1

M = int(input())
list_M = list(map(int,input().split()))

answer = []
for m in range(M):
    if list_N[list_M[m]] == 0:
        answer += ['0']
    else:
        answer += ['1']

print(' '.join(answer))