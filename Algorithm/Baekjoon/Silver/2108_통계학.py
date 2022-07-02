import sys
N = int(input())

num_cnt = [0] * 8001
all_list = []
total = 0
max_value = -2e29
min_value = 2e29
for n in range(N):
    now = int(sys.stdin.readline())
    num_cnt[now] += 1
    all_list.append(now)
    total += now
    max_value = max(max_value, now)
    min_value = min(min_value, now)

# 1. 산술평균
print(round(total / N))

# 2. 중앙값
all_list.sort()
print(all_list[len(all_list) // 2])

# 3. 최빈값
max_cnt = 0
for n in range(-4000, 4001, 1):
    if num_cnt[n]:
        if num_cnt[n] > max_cnt:
            max_cnt = num_cnt[n]
            tong = [n]
        elif num_cnt[n] == max_cnt:
            tong.append(n)
if len(tong) > 1:
    print(tong[1])
else:
    print(tong[0])

# 4. 범위
print(max_value - min_value)



