import heapq
N, M = map(int,input().split())
card_list = list(map(int,input().split()))
heap = []
for card in card_list:
    heapq.heappush(heap, card)
for m in range(M):
    alpha = heapq.heappop(heap)
    bravo = heapq.heappop(heap)
    new_num = alpha + bravo
    for i in range(2):
        heapq.heappush(heap, new_num)
print(sum(heap))