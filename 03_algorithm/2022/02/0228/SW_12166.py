def merge_sort(s, e):
    global cnt
    if s == e:
        return [A[s]]
    mid = (s + e) // 2
    left = merge_sort(s, mid)
    right = merge_sort(mid + 1, e)
    l_idx = 0
    r_idx = 0
    l_len = len(left)
    r_len = len(right)
    tmp = [0] * (l_len + r_len)
    idx = 0
    while l_idx < l_len and r_idx < r_len:
        if left[l_idx] > right[r_idx]:
            tmp[idx] = right[r_idx]
            r_idx += 1
            cnt += l_len - l_idx
        else:
            tmp[idx] = left[l_idx]
            l_idx += 1
        idx += 1
    while l_idx < l_len:
        tmp[idx] = left[l_idx]
        idx += 1
        l_idx += 1
    while r_idx < r_len:
        tmp[idx] = right[r_idx]
        idx += 1
        r_idx += 1
    return tmp


T = int(input())
for t in range(1,T+1):
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    merge_sort(0, N - 1)
    print('#{} {}'.format(t, cnt))
