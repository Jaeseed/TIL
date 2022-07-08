import sys
import heapq
N = int(input())
class_list = []
for n in range(N):
    S, T = map(int, sys.stdin.readline().split())
    class_list.append([T, S])
class_list.sort(key=lambda x: x[1])
heap = []
heapq.heappush(heap, class_list[0])
for n in range(1, N):
    T, S = heapq.heappop(heap)
    if class_list[n][1] >= T:
        T = class_list[n][0]
        heapq.heappush(heap,[T,S])
    else:
        heapq.heappush(heap,[T,S])
        heapq.heappush(heap,class_list[n])
print(len(heap))

