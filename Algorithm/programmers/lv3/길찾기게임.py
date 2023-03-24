import sys


def tmp(now, left, right, c, d):
    c.append(now)
    if left[now]:
        tmp(left[now], left, right, c, d)
    if right[now]:
        tmp(right[now], left, right, c, d)
    d.append(now)
    return


def solution(nodeinfo):
    sys.setrecursionlimit(2500)
    length = len(nodeinfo)
    num_list = [0] * 100001
    root = [-1, -1]
    for i in range(len(nodeinfo)):
        num_list[nodeinfo[i][0]] = i + 1
        if root[1] < nodeinfo[i][1]:
            root = nodeinfo[i]
    nodeinfo.sort(key=lambda x: x[0])
    left = [0] * (length + 1)
    right = [0] * (length + 1)
    stack = [nodeinfo[0]]
    for i in range(1, length):
        x, y = nodeinfo[i]
        if y > stack[-1][1]:
            while stack:
                if stack[-1][1] > y:
                    break
                sx, sy = stack.pop()
                if not stack:
                    left[num_list[x]] = num_list[sx]
                else:
                    if stack[-1][1] > y:
                        px = x
                    else:
                        px = stack[-1][0]
                    if sx > px:
                        right[num_list[px]] = num_list[sx]
                    else:
                        left[num_list[px]] = num_list[sx]
        stack.append([x, y])
    while len(stack) > 1:
        x, y = stack.pop()
        right[num_list[stack[-1][0]]] = num_list[x]
    #######
    a, b = [], []
    tmp(num_list[root[0]], left, right, a, b)
    print(a, b)
    return [a, b]


solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]])