T = int(input())
for t in range(T):
    N = int(input())
    list_ = list(map(int,input().split()))
    list_.sort(reverse=True)
    left = list_[0]
    right = list_[0]
    answer = 0
    if N % 2:
        flag = 0
        end = N
    else:
        flag = 1
        end = N - 1
    for n in range(1,end):
        if n % 2:
            answer = max(answer, left - list_[n])
            left = list_[n]
        else:
            answer = max(answer, right - list_[n])
            right = list_[n]
    if flag == 1:
        if left - list_[N-1] > right - list_[N-1]:
            answer = max(answer, right - list_[N-1])
            right = list_[N-1]
        else:
            answer = max(answer, left - list_[N-1])
            left = list_[N-1]
    answer = max(answer, abs(right - left))
    print(answer)
