'''
    1. L와 R의 자리수가 다르면 답은 0
        - L의 모든 자리를 9로 도배하거나 한자리 올려서 100 ~ 로 바꾸면 끝
    2. L와 R의 자리수가 같을 때
        1) 각 자리수의 값이 8로 같은 것만 앞에서부터 수를 센다
        2) 1번의 방식대로 처리하면 끝
'''

L, R = map(list, input().split())
answer = 0
if len(L) == len(R):
    for i in range(len(L)):
        if R[i] == L[i]:
            if R[i] == '8':
                answer += 1
        else:
            break
print(answer)