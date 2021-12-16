def heappush(tr,value):
    tr.append(value)
    node = len(tr)-1
    son_node = node
    while node > 1:
        node //= 2
        if tr[node] > value:
            tr[son_node] = tr[node]
            son_node = node
        else:
            break
    tr[son_node] = value
    return tr


def comparison(t, no):
    if len(t) - 1 >= no * 2 + 1:
        if t[no * 2] > t[no * 2 + 1]:
            return no * 2 + 1
        else:
            return no * 2
    elif len(t)-1 == no * 2:
        return no * 2
    else:
        return -1


def heappop(tr):
    if len(tr) == 1:
        return 0
    elif len(tr) == 2:
        return tr.pop()
    root = tr[1]
    target = tr.pop()
    tr[1] = target
    node = 1
    while True:
        pri_node = comparison(tr, node)
        if pri_node == -1:
            break
        if target > tr[pri_node]:
            tr[node] = tr[pri_node]
            node = pri_node
        else:
            break
    tr[node] = target
    return root


tree = [0]
a = [3,4,1,6,7,19,2,3]
for i in a:
    tree = heappush(tree, i)
for i in range(8):
    result = heappop(tree)