import sys
N = int(input())
works = []
for n in range(N):
    T, S = map(int, sys.stdin.readline().split())
    works.append([S, T])
works.sort()
answer = works[0][0] - works[0][1]
now_t = works[0][0]
if answer < 0:
    answer = -1
else:
    for i in range(1, N):
        s, t = works[i]
        if s - now_t < t:
            answer -= t + now_t - s
            if answer < 0:
                answer = -1
                break
            now_t = s
        else:
            now_t += t
print(answer)
