def str_to_idx(cha):
    return ord(cha) - ord('A')


def idx_to_chr(idx):
    return chr(idx + ord('A'))


def traversal(now):
    global preorder, inorder, postorder
    if now == -1:
        return
    preorder += idx_to_chr(now)
    traversal(left[now])
    inorder += idx_to_chr(now)
    traversal(right[now])
    postorder += idx_to_chr(now)
    return


N = int(input())
left = [-1] * 26
right = [-1] * 26
for n in range(N):
    p, l, r = input().split()
    parent = str_to_idx(p)
    if l != '.':
        le = str_to_idx(l)
        left[parent] = le
    if r != '.':
        ri = str_to_idx(r)
        right[parent] = ri
preorder = ''
inorder = ''
postorder = ''
traversal(0)
print(preorder)
print(inorder)
print(postorder)
