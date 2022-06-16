def dfs(value):
    global max_value
    global W
    if len(W) == 2:
        max_value = max(value, max_value)
        return
    copy_w = W[:]
    for i in range(1, len(W) - 1):
        W.pop(i)
        dfs(value + W[i-1] * W[i])
        W = copy_w[:]
    return


N = int(input())
W = list(map(int, input().split()))
max_value = 0
dfs(0)
print(max_value)
