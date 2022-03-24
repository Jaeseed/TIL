import sys

sys.stdin = open('input.txt', 'r')

dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]
blizzard_direction = {1: 3, 2: 1, 3: 0, 4: 2}


## MAP을 1차원 리스트로 바꾸기
def make_one_dimension():
    r = N // 2
    c = N // 2
    d = 0
    s = [1, 0]
    direction_cnt = 0
    for i in range(N ** 2 - 1):
        r, c, d, s, direction_cnt = direction_supporter(r, c, d, s, direction_cnt)
        new_map[i] = old_map[r][c]
        if old_map[r][c] == 0:
            break
    return


# 2차원 MAP의 인덱스 방향 맞추기
def direction_supporter(r, c, d, s, d_cnt):
    r += dr[d]
    c += dc[d]
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


## 얼음 파편 공격
# plus_list를 이용
def blizzard(d, s):
    nd = blizzard_direction[d]
    now_plus = 0
    # 등차수열 규칙 사용
    plus_list = [1, 1, 0, 0]
    total = -1
    for i in range(s):
        for j in range(4):
            now_plus += plus_list[j]
            # 방향 인덱스 잡기
            total += now_plus
            if new_map[total] == 0:
                return
            # 방향 같으면 파괴
            if j == nd:
                new_map[total] = 0
    return



def arrange():
    # 빈칸 점프량
    jump = 0
    # 현재 idx
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


def explosion():
    global exploded_gem
    is_exploded = False
    cnt = 1
    tong = [0]
    for i in range(0,(N ** 2) - 1):
        if new_map[i] == 0:
            break
        if new_map[i] == new_map[i + 1]:
            tong.append(i+1)
            cnt += 1
        else:
            # 폭발
            if cnt > 3:
                is_exploded = True
                for t in tong:
                    exploded_gem[new_map[t]] += new_map[t]
                    new_map[t] = 0
            # 초기화
            cnt = 1
            tong = [i+1]
    return is_exploded


def grouping():
    global new_map
    tmp = [0] * (N ** 2)
    idx = 0
    for i in range(0,(N ** 2) - 1, 2):
        if new_map[idx] == 0:
            break
        cnt = 1
        # 연속된 수 세기
        while True:
            if new_map[idx] == new_map[idx+1]:
                cnt += 1
                idx += 1
            else:
                # 새로운 리스트에 값 넣기
                tmp[i], tmp[i+1] = cnt, new_map[idx]
                idx += 1
                break
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

## 디버깅용 프린트 ##
    # print_idx = 0
    # print('--------')
    # for n in range(N):
    #     for p in range(print_idx, print_idx+N):
    #         print(new_map[p], end=' ')
    #     print_idx += N
    #     print()
    # print('------')

ans = 0
for key, value in exploded_gem.items():
    ans += value
print(ans)