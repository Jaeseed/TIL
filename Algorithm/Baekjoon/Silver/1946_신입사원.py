import sys

T = int(input())
for t in range(T):
    N = int(input())
    applicant_list = []
    for n in range(N):
        first, second = map(int,sys.stdin.readline().split())
        applicant_list.append([first,second])
    applicant_list.sort(key=lambda x:x[0])
    answer = 1
    min_second_score = applicant_list[0][1]
    for f, s in applicant_list:
        if s < min_second_score:
            answer += 1
            min_second_score = s
    print(answer)
