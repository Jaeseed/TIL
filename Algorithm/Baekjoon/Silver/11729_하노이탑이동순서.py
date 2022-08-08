def hanoi(n, s1, s2, s3):
    if n == 1:
        print(s1,s3)
        return
    hanoi(n-1, s1,s3,s2)
    print(s1,s3)
    hanoi(n-1, s2, s1, s3)


N = int(input())
answer = 0
for i in range(N):
    answer = answer * 2 + 1
print(answer)
hanoi(N, 1, 2, 3)