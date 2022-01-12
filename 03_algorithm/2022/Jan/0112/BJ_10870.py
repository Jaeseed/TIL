# N = int(input())
# now, new = 0, 1
# for n in range(N):
#     tmp_now = new
#     tmp_new = now + new
#     now, new = tmp_now, tmp_new
# print((now+new) * 2)

A = list(map(int,input()))
B = list(map(int,input()))
new_list = []
for i in range(8):
    new_list.append(A[i])
    new_list.append(B[i])
first_int = 0
last_int = 0
for f in range(8):
    first_int += new_list[f]
for l in range(8,16):
    last_int += new_list[l]
first_int %= 10
last_int %= 10
print(str(first_int)+str(last_int))