N, D = map(int,input().split())
distance = list(range(D+1))
shortcut = []
for n in range(N):
    s, e, d = map(int,input().split())
    if d >= e - s: continue
    if e > D: continue
    shortcut.append([s, e, d])
shortcut.sort(key=lambda x: x[1])
dp = list(range(D+1))
for idx in range(len(shortcut)):
    s, e, d = shortcut[idx]
    if dp[s] + d < dp[e]:
        tmp = dp[s] + d
        for d in range(e,D+1):
            dp[d] = tmp + d - e
print(dp[-1])