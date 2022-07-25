N = int(input())
distance = [0]
tmp = list(map(int,input().split()))
distance += tmp
costs = list(map(int,input().split()))
cost = costs[0]
answer = 0
for n in range(1,N):
    answer += cost * distance[n]
    if cost > costs[n]:
        cost = costs[n]
print(answer)
