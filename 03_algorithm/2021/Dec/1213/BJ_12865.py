# import time
def packing():
    global max_value
    idx = 0
    tong = []
    total_weight = 0
    total_value = 0
    while idx < N:
        w = things[idx][0]
        v = things[idx][1]
        if total_weight + w <= K:
            total_weight += w
            total_value += v
            tong.append([w,v])
            idx += 1
        else:
            flag = 0
            if max_value < total_value:
                max_value = total_value
            if len(tong) == 0:
                return
            before_weight = tong[-1][0]
            for i in range(idx,N):
                if things[i][0] > before_weight:
                    idx = i
                    flag = 1
                    break
            if flag == 0:
                return
            while total_weight + things[idx][0] > K:
                if len(tong) == 0:
                    return
                w, v = tong.pop()
                total_weight -= w
                total_value -= v
    if max_value < total_value:
        max_value = total_value
    return


N, K = map(int, input().split())
things = []
max_value = 0
for n in range(N):
    thing, weight = map(int, input().split())
    things.append([thing, weight])
# start = time.time()
things.sort(key=lambda x: (x[0], -x[1]))
packing()
print(max_value)
# print("time :", time.time() - start)
