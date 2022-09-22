import heapq, sys
N = int(input())
bundle_list = []
for i in range(N):
    bundle_list.append(int(sys.stdin.readline()))
heap = []
answer = 0

for j in range(N):
    heapq.heappush(heap, bundle_list[j])

for k in range(N-1):
    alpha = heapq.heappop(heap)
    bravo = heapq.heappop(heap)
    answer += alpha + bravo
    heapq.heappush(heap, alpha + bravo)
print(answer)