N = int(input())
A = list(map(int,input().split()))
l_distance = 0
r_distance = 0
l_cnt = 0
r_cnt = 0
for idx in range(N):
    l_value = A[idx]
    r_value = A[-idx-1]
    if l_value % 2:
        l_distance += idx - l_cnt
        l_cnt += 1
    if r_value % 2:
        r_distance += idx - r_cnt
        r_cnt += 1
print(min(l_distance, r_distance))
