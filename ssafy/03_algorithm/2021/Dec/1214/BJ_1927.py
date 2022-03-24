import sys
import heapq

N = int(sys.stdin.readline())
heap = []
for n in range(N):
    target = int(sys.stdin.readline())
    if target == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, target)
