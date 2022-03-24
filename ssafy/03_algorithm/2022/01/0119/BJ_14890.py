def horizontal_load(target):
    visited = [0] * N
    idx = 0
    while idx < N-1:
        now, next_ = MAP[target][idx], MAP[target][idx+1]
        if now == next_:
            idx += 1
            continue
        if abs(now - next_) > 1:
            return False
        tmp = idx
        if now > next_:
            value = 1
            height = next_
        else:
            value = -1
            tmp += 1
            height = now
        bridge = 0
        while 0 <= idx < N:
            tmp += value
            if tmp >= N or tmp < 0:
                return False
            if MAP[target][tmp] == height:
                if visited[tmp] == 1:
                    return False
                visited[tmp] = 1
                bridge += 1
                if bridge == L:
                    if tmp > idx:
                        idx = tmp
                    else:
                        idx += 1
                    break
            else:
                return False
    return True


def vertical_load(target):
    visited = [0] * N
    idx = 0
    while idx < N-1:
        now, next_ = MAP[idx][target], MAP[idx+1][target]
        if now == next_:
            idx += 1
            continue
        if abs(now - next_) > 1:
            return False
        tmp = idx
        if now > next_:
            value = 1
            height = next_
        else:
            value = -1
            tmp += 1
            height = now
        bridge = 0
        while 0 <= idx < N:
            tmp += value
            if tmp >= N or tmp < 0:
                return False
            if MAP[tmp][target] == height:
                if visited[tmp] == 1:
                    return False
                visited[tmp] = 1
                bridge += 1
                if bridge == L:
                    if tmp > idx:
                        idx = tmp
                    else:
                        idx += 1
                    break
            else:
                return False
    return True


N, L = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for row in range(N):
    if horizontal_load(row):
        ans += 1
for col in range(N):
    if vertical_load(col):
        ans += 1
print(ans)
