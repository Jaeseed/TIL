import sys

N, K = map(int,input().split())
coin = []
for n in range(N):
    coin.append(int(sys.stdin.readline()))
idx = N
answer = 0
while idx >= 0:
    idx -= 1
    now = coin[idx]
    if K < now:
        continue
    cnt = K // now
    K -= cnt * now
    answer += cnt
print(answer)