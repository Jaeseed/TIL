N = int(input())
cnt = 0
while True:
    now = N - 2 * cnt
    if now < 0:
        ans = -1
        break
    if now % 5 == 0:
        ans = cnt + now // 5
        break
    cnt += 1
print(ans)