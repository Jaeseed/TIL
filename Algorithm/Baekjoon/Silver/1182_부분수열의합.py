def find_S(step, num, total, path):
    global cnt
    if step == N:
        if num == 0:
            return
        if total == S:
            cnt += 1
        return
    find_S(step+1, num+1, total + arr[step], path + str(arr[step]))
    find_S(step+1, num, total, path)


N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

find_S(0, 0, 0, '')
print(cnt)