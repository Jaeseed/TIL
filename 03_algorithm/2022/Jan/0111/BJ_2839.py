N = int(input())
factor_5 = N // 5
factor_3 = 0
flag = 0
while factor_5 >= 0:
    now_value_5 = factor_5 * 5
    tmp = N - now_value_5
    if tmp == 0:
        flag = 1
        break
    if tmp % 3 == 0:
        factor_3 = tmp // 3
        flag = 1
        break
    factor_5 -= 1
if flag == 1:
    print(factor_5 + factor_3)
else:
    print(-1)

