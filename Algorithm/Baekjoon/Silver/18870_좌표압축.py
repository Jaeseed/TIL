N = int(input())
list_ = list(map(int,input().split()))
tong = []
answer = [0] * N
for idx, value in enumerate(list_):
    tong.append([idx, value])
tong.sort(key=lambda x:x[1])
past_value = tong[0][1]
idx = 0
for n in range(N):
    if tong[n][1] == past_value:
        answer[tong[n][0]] = idx
    else:
        idx += 1
        past_value = tong[n][1]
        answer[tong[n][0]] = idx
print(' '.join(map(str, answer)))