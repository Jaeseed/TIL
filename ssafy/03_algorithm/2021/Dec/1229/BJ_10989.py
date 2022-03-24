import sys
N = int(input())
arr = [0] * 10001
for n in range(N):
    now = int(sys.stdin.readline())
    arr[now] += 1
for i in range(1,10001):
    if arr[i] == 0: continue
    now = arr[i]
    while now > 0:
        print(i)
        now -= 1