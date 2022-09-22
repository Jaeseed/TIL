import heapq
T = int(input())
for t in range(T):
    K = int(input())
    chapter = list(map(int,input().split()))
    heap = []
    answer = 0
    for c in chapter:
        heapq.heappush(heap, c)
    while len(heap) > 1:
        now1 = heapq.heappop(heap)
        now2 = heapq.heappop(heap)
        answer += now1 + now2
        heapq.heappush(heap, now1 + now2)
    print(answer)
