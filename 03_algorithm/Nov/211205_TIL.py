import sys
sys.stdin = open('input.txt' , 'r')


def dfs(days,now_income):
    global max_income
    if days > N:
        return
    if (days + counsel_list[days][0]) > N+1:
        max_income = max(max_income, now_income)
    elif (days + counsel_list[days][0]) == N+1:
        max_income = max(max_income, now_income + counsel_list[days][1])
    else:
        dfs(days + counsel_list[days][0], now_income + counsel_list[days][1])
    dfs(days + 1, now_income)


N = int(input())
counsel_list = [0]
for n in range(N):
    day, income = map(int, input().split())
    counsel_list.append([day,income])
max_income = 0
dfs(1, 0)
print(max_income)