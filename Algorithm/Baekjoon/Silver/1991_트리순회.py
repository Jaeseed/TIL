def dfs(now):
    global preorder, inorder, postorder
    if now == -1:
        return
    preorder += chr(now + 65)
    dfs(left[now])
    inorder += chr(now + 65)
    dfs(right[now])
    postorder += chr(now + 65)


N = int(input())
left = [-1] * N
right = [-1] * N
preorder, inorder, postorder = '', '', ''
for n in range(N):
    me, l, r = input().split()
    if l != '.':
        left[ord(me) - 65] = ord(l) - 65
    if r != '.':
        right[ord(me) - 65] = ord(r) - 65
dfs(0)
print(preorder)
print(inorder)
print(postorder)
