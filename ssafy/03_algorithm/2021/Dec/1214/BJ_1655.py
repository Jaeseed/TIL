import sys
import heapq
N = int(sys.stdin.readline())
heap_left = []
heap_right = []
for n in range(N):
    target = int(sys.stdin.readline())
    if len(heap_left) == len(heap_right):
        heapq.heappush(heap_left, (-target, target))
    else:
        heapq.heappush(heap_right, target)
    while True:
        if len(heap_right) == 0:
            break
        elif heap_left[0][1] > heap_right[0]:
            dump, left = heapq.heappop(heap_left)
            right = heapq.heappop(heap_right)
            heapq.heappush(heap_left, (-right,right))
            heapq.heappush(heap_right, left)
        else:
            break
    print(heap_left[0][1])