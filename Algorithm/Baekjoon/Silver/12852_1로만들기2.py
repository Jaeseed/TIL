from heapq import heappush, heappop


def find_route():
    qu = []
    heappush(qu, [0, N, []])
    while True:
        cnt, now, route = heappop(qu)
        if now == 1:
            return route
        for i in range(3, 1, -1):
            if now % i == 0:
                tmp = now // i
                heappush(qu,[cnt + 1, tmp, route + [now]])
            if (now - 1) % i == 0:
                tmp = (now - 1) // i
                heappush(qu, [cnt + 2, tmp, route + [now, now - 1]])
            if (now - 2) % i == 0:
                tmp = (now - 2) // i
                heappush(qu, [cnt + 3, tmp, route + [now, now - 1, now - 2]])



N = int(input())
if N == 1:
    print(0)
    print(1)
else:
    ret = find_route()
    print(len(ret))
    print(*ret + [1])
