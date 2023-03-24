"""
case 1:
    K = 1 일 때
    answer = 2 ** (max_bit) - N

case 2:
    K > 1 이고 빈 공간을 만들 수 없을 때 ( ex) N = 0b11110, K = 3)
    11100 K = 2 -> 100000
    answer = 2 ** (max_bit) - N ( case 1 과 같은 방식)

case 3:
    K > 1 이고 빈 공간을 만들 수 있을 때 ( ex) N = 0b10111 K = 3)
    answer =
"""


N, K = map(int,input().split())
# 현재 N의 2진법 비트 중 가장 최상위 비트 위치
max_bit = 0
tmp = N
while True:
    tmp //= 2
    if tmp == 0:
        break
    max_bit += 1
# N을 2진법화
binary_list = []
# K값과 비교 변수
not_empty_bottle = 0
# 물병 추가 필요 유무 확인 (flag == 0 => 물병 추가 필요X)
flag = 0
answer = 0
for m in range(max_bit, -1, -1):
    if N & (1 << m):
        not_empty_bottle += 1
        if not_empty_bottle > K:
            flag = 1
            break
        binary_list.append(1)
    else:
        binary_list.append(0)
if flag:
    # 채워진 마지막 물병 찾기
    while binary_list[-1] == 0:
        binary_list.pop()
    # 빈 물병을 찾고 그 뒤는 모조리 제거
    while binary_list and binary_list[-1]:
        binary_list.pop()

    # 모두 채워졌을 땐 max_bit + 1
    if not binary_list:
        answer = (1 << (max_bit + 1)) - N
    else:
        target = 0
        binary_list[-1] = 1
        for b in binary_list:
            target += b << max_bit
            max_bit -= 1
        answer = target - N
print(answer)