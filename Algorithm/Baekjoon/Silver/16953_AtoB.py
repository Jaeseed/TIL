start, target = map(int,input().split())
answer = 1

while True:
    if start > target:
        answer = -1
        break
    if start == target:
        break
    if target % 10 == 1:
        target //= 10
    else:
        if target % 2:
            answer = -1
            break
        target //= 2
    answer += 1
print(answer)