import sys


def find(man):
    global parent_list
    if parent_list[man] == man:
        return man
    pm = find(parent_list[man])
    parent_list[man] = pm
    parent_list[man] = min(parent_list[pm], parent_list[man])
    return pm


def union(s1, s2):
    global parent_list
    ps1 = find(s1)
    ps2 = find(s2)
    parent_list[ps2] = ps1
    parent_list[ps2] = min(parent_list[ps1], parent_list[ps2])
    return


N, M, K = map(int, input().split())
costs = list(map(int, input().split()))
parent_list = list(range(N+1))
for m in range(M):
    f1, f2 = map(int, sys.stdin.readline().split())
    union(f1,f2)

# union 관계 정리
for n in range(1, N+1):
    find(n)

costs_result = [0] * (N+1)
# cost 찾기
for now in range(1,N+1):
    p_now = parent_list[now]
    if costs_result[p_now] == 0:
        costs_result[p_now] = costs[now-1]
    else:
        costs_result[p_now] = min(costs[now-1], costs_result[p_now])
if sum(costs_result) > K:
    print('Oh no')
else:
    print(sum(costs_result))
