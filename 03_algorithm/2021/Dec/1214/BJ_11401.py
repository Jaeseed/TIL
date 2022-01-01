N, K = map(int, input().split())
N_list = []
K_list = []
if N - K < N // 2:
    N_list = [n for n in range(N, K, -1)]
    K_list = [k for k in range(1, N - K + 1)]
else:
    N_list = [n for n in range(N, N - K, -1)]
    K_list = [k for k in range(1, K + 1)]
len_N = len(N_list)
len_K = len(K_list)
idx = len_K - 1
while idx > 0:
    target = K_list[idx]
    if N % target == 0:
        N_list[0] //= target
    else:
        tmp = N % target
        if N_list[tmp] % target == 0:
            N_list[tmp] //= target
        else:
            if target % N_list[tmp] == 0:
                K_list[idx] //= N_list[tmp]
                N_list[tmp] = 1
                continue
            tong = [tmp]
            value = N_list[tmp]
            while True:
                if value % target == 0:
                    for t in tong:
                        N_list[t] = 1
                    N_list[tmp] = value // target
                    break
                tmp += target
                tong.append(tmp)
                value *= N_list[tmp]
    idx -= 1
value = 1
for i in N_list:
    if i == 0:
        break
    value *= i
    if value >= 1000000007:
        value %= 1000000007
    if value == 0:
        value = 1
print(value)
