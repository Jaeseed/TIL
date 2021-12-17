N, K = map(int,input().split())
line = list(input())
ans = 0
for i in range(N):
    if line[i] == 'P':
        adj = -K
        while adj <= K:
            if i + adj < 0:
                adj += 1
                continue
            elif i + adj >= N:
                break
            elif line[i+adj] == 'H':
                ans += 1
                line[i+adj] = 0
                break
            else:
                adj += 1
print(ans)