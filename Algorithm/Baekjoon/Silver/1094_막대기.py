from heapq import heappop, heappush
X = int(input())
h = []
heappush(h, 64)
while True:
    if sum(h) == X:
        answer = len(h)
        break
    smallest = heappop(h)
    half = smallest // 2
    heappush(h, half)
    if sum(h) > X:
        continue
    elif sum(h) == X:
        continue
    else:
        heappush(h, half)
print(answer)