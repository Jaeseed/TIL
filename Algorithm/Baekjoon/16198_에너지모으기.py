def dfs(value):
    global max_value
    if len(W) == 2:
        max_value = max(value, max_value)
    copy_w = W[:]
    for i in range(1,len(W)-1):
        
    return


N = int(input())
W = list(map(int,input().split()))
max_value = 0
dfs(0)