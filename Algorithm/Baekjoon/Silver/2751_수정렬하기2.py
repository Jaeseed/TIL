import sys


def distribution(s, e):
    if s == e:
        return [list_[s]]
    a = distribution(s, (s + e) // 2)
    b = distribution((s + e) // 2 + 1, e)
    len_a = len(a)
    len_b = len(b)
    now_a = 0
    now_b = 0
    now_list = []
    while now_a < len_a and now_b < len_b:
        if a[now_a] > b[now_b]:
            now_list.append(b[now_b])
            now_b += 1
        else:
            now_list.append(a[now_a])
            now_a += 1
    if now_a < len_a:
        while now_a < len_a:
            now_list.append(a[now_a])
            now_a += 1
    elif now_b < len_b:
        while now_b < len_b:
            now_list.append(b[now_b])
            now_b += 1
    return now_list


def my_sort():
    return


N = int(input())
list_ = []
for n in range(N):
    now = int(sys.stdin.readline())
    list_.append(now)
answer = distribution(0, N-1)
for n in answer:
    print(n)
