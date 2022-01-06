def union(p, s):
    pa = find_parent(p)
    pb = find_parent(s)
    if pa != pb:
        parent_list[pb] = pa


def find_parent(unit):
    if parent_list[unit] == unit:
        return unit
    ret = find_parent(parent_list[unit])
    parent_list[unit] = ret
    return ret


def is_possible_for_arive():
    for i in range(len(plan) - 1):
        now, ne_xt = plan[i], plan[i + 1]
        p_now = find_parent(now)
        p_next = find_parent(ne_xt)
        if p_now != p_next:
            return False
    return True


N = int(input())
M = int(input())
adj = [[0] * (N + 1)]
for _ in range(1, N + 1):
    adj.append(list(map(int, ('0 ' + input()).split())))
plan = list(map(int, input().split()))
parent_list = list(range(N + 1))
for row in range(1, N + 1):
    for col in range(1, N + 1):
        if adj[row][col] == 1:
                union(row, col)
if is_possible_for_arive():
    print('YES')
else:
    print('NO')


