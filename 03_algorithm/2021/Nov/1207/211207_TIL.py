import sys

sys.stdin = open('input.txt', 'r')

# 블리자드 이외 모든 방향용 리스트
adr = [0, 1, 0, -1]
adc = [-1, 0, 1, 0]
blizzard_direction = {1: 3, 2: 1, 3: 0, 4: 2}


def make_one_dimension():
    r = N // 2
    c = N // 2
    d = 0
    s = [1, 0]
    direction_cnt = 0
    for i in range(N ** 2):
        r, c, d, s, direction_cnt = direction_supporter(r, c, d, s, direction_cnt)
        new_map[i] = old_map[r][c]
        if old_map[r][c] == 0:
            break
    return


def blizzard(d, s):
    nd = blizzard_direction[d]
    now_plus = 0
    plus_list = [1, 1, 0, 0]
    total = -1
    for i in range(s):
        for j in range(4):
            now_plus += plus_list[j]
            total += now_plus
            if new_map[total] == 0:
                return
            if j == nd:
                new_map[total] = 0
    return



def arrange():
    jump = 0
    now = 0
    while now + jump < N ** 2:
        if new_map[now]:
            now += 1
        else:
            tmp = now + jump
            while tmp < N ** 2:
                if new_map[tmp]:
                    break
                tmp += 1
                jump += 1
            if tmp == N ** 2:
                return
            new_map[now], new_map[now+jump] = new_map[now+jump], new_map[now]
    return


def direction_supporter(r, c, d, s, d_cnt):
    r += adr[d]
    c += adc[d]
    s[1] += 1
    if s[0] == s[1]:
        s[1] = 0
        d_cnt += 1
        d += 1
        d %= 4
        if d_cnt == 2:
            s[0] += 1
            d_cnt = 0
    return r, c, d, s, d_cnt


def explosion():
    global exploded_gem
    is_exploded = False
    before = new_map[0]
    now = 0
    cnt = 0
    idx = 0
    tong = []
    while new_map[idx] != 0 and idx < N ** 2:
        now = new_map[idx]
        if before == now:
            cnt += 1
            tong.append(idx)
        else:
            if cnt > 3:
                is_exploded = True
                for t in tong:
                    exploded_gem[new_map[t]] += new_map[t]
                    new_map[t] = 0
                tong = []
                cnt = 0
            else:
                tong = [idx]
                cnt = 1
        before = now
        idx += 1
    return is_exploded


def grouping():
    global new_map
    tmp = [0] * (N ** 2)
    before = new_map[0]
    now = 0
    idx = 0
    cnt = 0
    for i in range(0,(N ** 2) - 1, 2):
        if new_map[idx] == 0:
            break
        cnt = 1
        while True:
            now = new_map[idx]
            if before == now:
                cnt += 1
                idx += 1
            else:
                number = before
                before = now
                idx += 1
                break
        tmp[i], tmp[i+1] = cnt, number
    new_map = tmp[:]
    return


N, M = map(int, input().split())
old_map = [list(map(int, input().split())) for _ in range(N)]
new_map = [0] * (N ** 2)
make_one_dimension()
magic_list = [list(map(int, input().split())) for _ in range(M)]
exploded_gem = {1: 0, 2: 0, 3:0}
for direction, space in magic_list:
    blizzard(direction, space)
    arrange()
    while True:
        ret = explosion()
        if ret == False:
            break
        arrange()
    grouping()
    print_idx = 0
    print('--------')
    for n in range(N):
        for p in range(print_idx, print_idx+N):
            print(new_map[p], end=' ')
        print_idx += N
        print()
    print('------')
print(exploded_gem)
ans = sum(exploded_gem)
print(ans)
