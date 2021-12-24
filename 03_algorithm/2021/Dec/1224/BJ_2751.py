import sys
N = int(input())
num_list = []
for n in range(N):
    num_list.append(int(sys.stdin.readline()))
num_list.sort()
for n in range(N):
    print(num_list[n])