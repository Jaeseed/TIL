N = int(input())
num_list = list(map(int, input().split()))
# A부터 인접한 주사위 칸의 인덱스 저장
adj_idx = [
    [1, 2, 4, 3],
    [0, 2, 5, 3],
    [0, 1, 5, 4],
    [0, 1, 5, 4],
    [0, 2, 5, 3],
    [1, 2, 4, 3]
]

# 1. 주사위 위치별 최소값 구하기
# 1-1. 한 값의 최소값
one_min = min(num_list)

# 1-2. 두 값의 최소값
two_min = 2e29
for i in range(6):
    now = num_list[i]
    for j in range(4):
        two_min = min(two_min, now + num_list[adj_idx[i][j]])

# 1-3. 세 값의 최소값
three_min = 2e29
for i in range(6):
    now = num_list[i]
    for j in range(4):
        three_min = min(three_min, now + num_list[adj_idx[i][j]] + num_list[adj_idx[i][(j + 1) % 4]])

answer = 0
# N이 1일 때 가지치기
if N == 1:
    print(sum(num_list) - max(num_list))
else:
    # 2. 윗면 최소 구하기
    top_width = N
    # 2-1. 3개면이 보이는 각 꼭지점 4개 털기
    answer += three_min * 4
    top_width -= 2
    # 2-2. 2개면 털기
    answer += two_min * top_width * 4
    # 2-3. 한면 털기
    answer += one_min * top_width * top_width

    # 3. 옆면 최소 구하기
    side_height = N - 1
    side_width = N - 2
    # 3-1 모서리의 두 면 주사위 털기
    answer += two_min * side_height * 4
    # 3-2 한 면 주사위 털기
    answer += one_min * side_width * side_height * 4
    print(answer)


