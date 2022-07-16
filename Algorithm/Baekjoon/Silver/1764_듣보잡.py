import sys
N, M = map(int,input().split())
tong = set()
real_stranger = []
for n in range(N):
    stranger = sys.stdin.readline()
    tong.add(stranger)
for m in range(M):
    cnt = len(tong)
    stranger = sys.stdin.readline()
    tong.add(stranger)
    if len(tong) == cnt:
        real_stranger.append(stranger)
real_stranger.sort()
print(len(real_stranger))
print(''.join(real_stranger))