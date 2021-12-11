def make_six(step, before):
    global tong
    if step == 6:
        print(' '.join(map(str, tong)))
        return
    for k in range(before, K+1):
        if visited[k] == 0:
            visited[k] = 1
            tong.append(input_list[k])
            make_six(step+1, k)
            visited[k] = 0
            tong.pop()
    return


input_list = list(map(int,input().split()))
K = input_list[0]
visited = [0] * (K + 1)
tong = []
make_six(0, 1)
