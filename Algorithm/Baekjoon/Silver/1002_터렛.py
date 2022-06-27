T = int(input())
for t in range(T):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1/2)
    if distance == 0:
        if r1 != r2:
            answer = 0
        else:
            answer = -1
    else:
        if r1 + r2 == distance or r1 + distance == r2 or r2 + distance == r1:
            answer = 1
        elif r1 + distance < r2 or r2 + distance < r1:
            answer = 0
        elif r1 + r2 < distance:
            answer = 0
        else:
            answer = 2
    print(answer)