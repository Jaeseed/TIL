fuel_distance = int(input())
N = int(input())
distance_list = list(map(int,input().split()))
time_list = [0]
time_list += list(map(int,input().split()))
time_list += [0]
dp = [[time_list[_],[]] for _ in range(N+2)]
dp[0][0] = 0
for i in range(1, N+2):
    idx = i - 1
    used_distance = distance_list[idx]
    min_time = 2e29
    while used_distance <= fuel_distance and idx >= 0:
        if min_time > time_list[i] + dp[idx][0]:
            min_time = time_list[i] + dp[idx][0]
            min_route = dp[idx][1] + [i]
        idx -= 1
        used_distance += distance_list[idx]
    dp[i][0] = min_time
    dp[i][1] = min_route
print(dp[-1][0])
if dp[-1][1] == [N+1]:
    print(0)
else:
    answer = dp[-1][1]
    answer.pop()
    print(len(answer))
    print(*answer)