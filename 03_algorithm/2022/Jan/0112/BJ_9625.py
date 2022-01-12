K = int(input())
cnt_A = 1
cnt_B = 0
for k in range(K):
    tmp_A = cnt_B
    tmp_B = cnt_A + cnt_B
    cnt_A, cnt_B = tmp_A, tmp_B
print(cnt_A, cnt_B)
