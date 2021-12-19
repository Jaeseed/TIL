N = int(input())
i_list = list(map(int,input().split()))
M = int(input())
t_list = list(map(int,input().split()))
i_list.sort()
for t in t_list:
    front = 0
    end = N-1
    now = N // 2
    while True:
        if i_list[now] < t:
            tmp = now
            front = now + 1
            now = (now + 1 + end) // 2
        elif i_list[now] > t:
            tmp = now
            end = now - 1
            now = (now -1 + front) // 2
        else:
            print(1)
            break
        if tmp == now:
            print(0)
            break