N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))
ans_list = [0] * M
all_list = [0] * 20000001
for n in N_list:
    all_list[n] = 1
idx = 0
for m in M_list:
    if all_list[m]:
        ans_list[idx] = '1'
    else:
        ans_list[idx] = '0'
    idx += 1
print(' '.join(ans_list))