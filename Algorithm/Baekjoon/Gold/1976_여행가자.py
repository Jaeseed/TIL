def union(a,b):
    global parent_list
    pa = find(a)
    pb = find(b)
    parent_list[pb] = pa
    return


def find(city):
    global parent_list
    if parent_list[city] == city:
        return city
    p_city = find(parent_list[city])
    parent_list[city] = p_city
    return p_city


N = int(input())
M = int(input())
MAP = [list(map(int,input().split())) for _ in range(N)]
plan = list(map(int,input().split()))
parent_list = list(range(N+1))
for i in range(N):
    for j in range(i+1, N):
        if MAP[i][j] == 0: continue
        union(i+1,j+1)
for check in range(1, N+1):
    find(check)
flag = 1
for p in range(len(plan)-1):
    if parent_list[plan[p]] != parent_list[plan[p+1]]:
        flag = 0
        break
if flag == 1:
    print('YES')
else:
    print('NO')