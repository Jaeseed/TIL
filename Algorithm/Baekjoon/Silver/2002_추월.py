import sys
N = int(input())
# 입장 차량
entrance_dict = {}
# 퇴장 차량
exit_dict = {}
# 순서마다 가지는 추월 차량 수
overtake_list = [0] * N
# 총 추월차량 수
overtake_cnt = 0
## 입구와 출구 딕셔너리를 key value 반대로 지정
for n in range(N):
    entrance_dict[n] = sys.stdin.readline()
for n in range(N):
    exit_dict[sys.stdin.readline()] = n

for n in range(N-1,-1,-1):
    # 추월차량 수 + 원래 순서와 다를 시 분기처리
    exit_order = exit_dict[entrance_dict[n]]
    if n + overtake_list[exit_order] != exit_order:
        overtake_cnt += 1
        passing_idx = exit_order
        for m in range(passing_idx,N):
            overtake_list[m] += 1
print(overtake_cnt)