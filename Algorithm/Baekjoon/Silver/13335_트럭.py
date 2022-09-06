# N = 트럭 수, W = 길이, L = 하중
N, W, L = map(int,input().split())
truck_list = list(map(int,input().split()))
crossing_bridge_truck = []
crossing_bridge_truck.append([truck_list[0], 1])
# 대기 중인 truck_list idx
waiting_idx = 1
# 다리에 올라탄 crossing_bridge idx
crossing_idx = 0
now_weight = truck_list[0]
cnt = 1
answer = 1
# 트럭이 다리 위에 올라와도 되는지 여부
flag = 1
# 트럭이 다 다리 위에 있거나 지나갔을 때까지
while waiting_idx < N:
    for i in range(crossing_idx, len(crossing_bridge_truck)):
        crossing_bridge_truck[i][1] += 1
        if crossing_bridge_truck[i][1] > W:
            cnt -= 1
            now_weight -= crossing_bridge_truck[i][0]
            crossing_idx += 1
            # 재갱신
            flag = 1
    if cnt < W and flag == 1:
        if truck_list[waiting_idx] + now_weight <= L:
            crossing_bridge_truck.append([truck_list[waiting_idx], 1])
            now_weight += truck_list[waiting_idx]
            cnt += 1
            waiting_idx += 1
        else:
            flag = 0
    answer += 1
answer += W - crossing_bridge_truck[-1][1] + 1
print(answer)