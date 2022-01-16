T = int(input())
for t in range(T):
    N,M = map(int,input().split())
    ans = 1
    for i in range(M,M-N,-1):
        ans *= i
    for j in range(2,N+1):
        ans //= j
    print(ans)