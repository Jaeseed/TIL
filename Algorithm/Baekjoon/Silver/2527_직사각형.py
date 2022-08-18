# 총 4개의 케이스
for t in range(4):
    # 직사각형 좌표 입력
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int,input().split())
    # 1) 한 점에서 만나는 경우 / c
    if (x1 == p2 and y1 == q2) or (x2 == p1 and y2 == q1) or (y1 == q2 and p1 == x2) or (y2 == q1 and p2 == x1):
        print('c')
        continue
    # 2) 분리된 경우 / d
    elif p1 < x2 or p2 < x1 or q1 < y2 or q2 < y1:
        print('d')
        continue
    # 3) 선분에서 만나는 경우 / b
    # 3-1) 좌우로 만나는 경우
    elif p1 == x2 and (y1 <= y2 <= q1 or y1 <= q2 <= q1 or y2 <= y1 <= q2 or y2 <= q1 <= q2):
        print('b')
        continue
    elif p2 == x1 and (y1 <= y2 <= q1 or y1 <= q2 <= q1 or y2 <= y1 <= q2 or y2 <= q1 <= q2):
        print('b')
        continue
    # 3-2) 상하로 만나는 경우
    elif q1 == y2 and (x1 <= x2 <= p1 or x1 <= p2 <= p1 or x2 <= x1 <= p2 or x2 <= p1 <= p2):
        print('b')
        continue
    elif q2 == y1 and (x1 <= x2 <= p1 or x1 <= p2 <= p1 or x2 <= x1 <= p2 or x2 <= p1 <= p2):
        print('b')
        continue
    print('a')