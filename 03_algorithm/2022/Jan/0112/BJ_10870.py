# N = int(input())
# now, new = 0, 1
# for n in range(N):
#     tmp_now = new
#     tmp_new = now + new
#     now, new = tmp_now, tmp_new
# print((now+new) * 2)


N = int(input())
pPAp = list(input())
answer_sheet = 'pPAp'
ans = 0
idx = 0
unit_idx = 0
while idx < N:
    if pPAp[idx] == answer_sheet[unit_idx]:
        if unit_idx == 3:
            ans += 1
            idx += 1
            unit_idx = 0
            continue
        idx += 1
        unit_idx += 1
    else:
        if unit_idx:
            unit_idx = 0
        else:
            idx += 1
print(ans)