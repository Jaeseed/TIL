import sys
N = int(input())
meeting = []
for n in range(N):
    s, e = map(int,sys.stdin.readline().split())
    meeting.append([s,e])
meeting.sort(key=lambda x: (x[1], x[0]))
end = meeting[0][1]
answer = 1
for n in range(1, N):
    if meeting[n][0] >= end:
        end = meeting[n][1]
        answer += 1
print(answer)