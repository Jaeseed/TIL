N, K = map(int, input().split())
container = list(map(int, input().split()))
robot_location_list = [0] * N
broken_box_cnt = 0
step = 0
while broken_box_cnt < K:
    step += 1
    container = [container[2*N-1]] + container[:2*N-1]
    robot_location_list = [robot_location_list[N-1]] + robot_location_list[:N-1]
    for ro in range(N-1, -1, -1):
        if robot_location_list[ro]:
            if ro == N - 1:
                robot_location_list[ro] = 0
            elif ro == N - 2 and container[ro + 1]:
                container[ro + 1] -= 1
                if container[ro + 1] == 0:
                    broken_box_cnt += 1
                robot_location_list[ro] = 0
            elif robot_location_list[ro + 1] == 0 and container[ro + 1]:
                robot_location_list[ro] = 0
                robot_location_list[ro + 1] = 1
                container[ro + 1] -= 1
                if container[ro + 1] == 0:
                    broken_box_cnt += 1
    if container[0]:
        robot_location_list[0] = 1
        container[0] -= 1
        if container[0] == 0:
            broken_box_cnt += 1
print(step)