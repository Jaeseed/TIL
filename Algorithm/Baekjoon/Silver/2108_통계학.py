import sys
import math
N = int(input())

list_ = [0] * 8001
set_ = set()
total = 0
max_value = -2e29
min_value = 2e29
for n in range(N):
    now = int(sys.stdin.readline())
    list_[now] += 1
    set_.add(now)
    total += now
    max_value = max(max_value, now)
    min_value = min(min_value, now)

# 1. 산술평균
print(round(total / N))

# 2. 중앙값
set_to_list = list(set_)
set_to_list.sort()
print(set_to_list[len(set_to_list) // 2])

# 3. 최빈값
max_cnt = 0
for n in range(len(list_)):
    if now > 4000:
        now = 8000 - n
    else:
        now = n
    if list_[now]:
        if list_[now] > max_cnt:
            max_cnt = list_[now]
            tong = [now]
        elif list_[now] == max_cnt:
            tong.append(now)
print(tong[1])

# 4. 범위
print(max_value - min_value)



