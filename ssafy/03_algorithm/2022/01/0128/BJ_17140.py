import heapq


def arrange_r():
    global len_c
    max_c = 0
    for r in range(len_r):
        heap = []
        tmp = [0] * 101
        for c in range(len_c):
            if A[r][c] > 0:
                tmp[A[r][c]] += 1
        for i in range(1, 101):
            if tmp[i]:
                tmp_cnt = tmp[i]
                heapq.heappush(heap, [tmp_cnt, i])
        tong = []
        heap2 = []
        while heap:
            cnt, value = heapq.heappop(heap)
            if not heap2:
                heapq.heappush(heap2,[value,cnt])
            elif len(heap2) == 1 and heap2[-1][1] != cnt:
                nv, nc = heapq.heappop(heap2)
                tong += [nv,nc]
                heapq.heappush(heap2,[value,cnt])
            elif heap2[-1][1] == cnt:
                heapq.heappush(heap2,[value,cnt])
            else:
                while heap2:
                    nnv, nnc = heapq.heappop(heap2)
                    tong += [nnv, nnc]
                heapq.heappush(heap2, [value, cnt])
        while heap2:
            nnv, nnc = heapq.heappop(heap2)
            tong += [nnv, nnc]
        A[r] = tong[:]
        max_c = max(max_c, len(A[r]))
    len_c = max_c
    for r in range(len_r):
        if len(A[r]) < len_c:
            difference = len_c - len(A[r])
            A[r] += [0] * difference
    return


def arrange_c():
    global len_r
    global len_c
    global A
    max_r = 0
    sub_A = [[0] for _ in range(len_c)]
    for c in range(len_c):
        heap = []
        tmp = [0] * 101
        for r in range(len_r):
            if A[r][c] > 0:
                tmp[A[r][c]] += 1
        for i in range(1,101):
            if tmp[i]:
                tmp_cnt = tmp[i]
                heapq.heappush(heap, [tmp_cnt,i])
        tong = []
        heap2 = []
        while heap:
            cnt, value = heapq.heappop(heap)
            if not heap2:
                heapq.heappush(heap2,[value,cnt])
            elif len(heap2) == 1 and heap2[-1][1] != cnt:
                nv, nc = heapq.heappop(heap2)
                tong += [nv,nc]
                heapq.heappush(heap2, [value, cnt])
            elif heap2[-1][1] == cnt:
                heapq.heappush(heap2,[value,cnt])
            else:
                while heap2:
                    nnv, nnc = heapq.heappop(heap2)
                    tong += [nnv, nnc]
                heapq.heappush(heap2, [value, cnt])
        while heap2:
            nnv, nnc = heapq.heappop(heap2)
            tong += [nnv, nnc]
        sub_A[c] = tong[:]
        max_r = max(max_r, len(sub_A[c]))
    len_r = max_r
    for c in range(len_c):
        if len(sub_A[c]) < len_r:
            difference = len_r - len(sub_A[c])
            sub_A[c] += [0] * difference
    A = [[0] * len_c for _ in range(len_r)]

    for r in range(len_r):
        for c in range(len_c):
            A[r][c] = sub_A[c][r]
    return


R, C, K = map(int,input().split())
R -= 1
C -= 1
A = [list(map(int,input().split())) for _ in range(3)]
seconds = 0
len_r = 3
len_c = 3
while True:
    if len_r > R and len_c > C and A[R][C] == K:
        break
    if seconds == 100:
        seconds = -1
        break
    if len_r >= len_c:
        arrange_r()
    else:
        arrange_c()
    seconds += 1
print(seconds)