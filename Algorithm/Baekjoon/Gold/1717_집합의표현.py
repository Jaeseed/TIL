import sys


def union(s1,s2):
    global parent_list
    p_s1 = find(s1)
    p_s2 = find(s2)
    parent_list[p_s2] = p_s1
    return


def find(s):
    if parent_list[s] == s:
        return s
    parent = find(parent_list[s])
    parent_list[s] = parent
    return parent


N, M = map(int,input().split())
parent_list = list(range(N+1))
for m in range(M):
    order, a, b = map(int,sys.stdin.readline().split())
    if order == 1:
        p_a = find(a)
        p_b = find(b)
        if p_a == p_b:
            print('YES')
        else:
            print('NO')
    else:
        union(a, b)