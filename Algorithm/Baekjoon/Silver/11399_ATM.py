N = int(input())
men = list(map(int,input().split()))
men.sort()
now = 0
answer = 0
for n in range(N):
    now += men[n]
    answer += now
print(answer)