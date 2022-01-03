N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
variation_list = [[1, N, 1], [N - 2, -1, -1]]


def dfs(step, order):
    if step == 5:
        play_game(order)
        return
    for i in range(4):
        dfs(step + 1, order + str(i))
    return


def play_game(direction_list):
    global max_value
    idx = 0
    now_map = [[0] * N for _ in range(N)]
    now_max_value = 0
    for r in range(N):
        for c in range(N):
            now_map[r][c] = MAP[r][c]
            now_max_value = max(now_max_value,now_map[r][c])
    while idx < 5:
        direction = int(direction_list[idx])
        v1, v2, v3 = variation_list[direction % 2][0], variation_list[direction % 2][1], variation_list[direction % 2][
            2]
        di = 1
        if direction % 2:
            di = -1
        if direction < 2:
            for c in range(N):
                now = v1 - di
                for r in range(v1, v2, v3):
                    if now_map[r][c] == 0:
                        continue
                    else:
                        if now_map[now][c] == 0:
                            now_map[now][c] = now_map[r][c]
                            now_map[r][c] = 0
                        else:
                            if now_map[now][c] == now_map[r][c]:
                                now_map[now][c] *= 2
                                now_max_value = max(now_max_value, now_map[now][c])
                                now_map[r][c] = 0
                                now += di
                            else:
                                if r == now + di:
                                    now += di
                                else:
                                    now += di
                                    now_map[now][c] = now_map[r][c]
                                    now_map[r][c] = 0
        else:
            for r in range(N):
                now = v1 - di
                for c in range(v1, v2, v3):
                    if now_map[r][c] == 0:
                        continue
                    else:
                        if now_map[r][now] == 0:
                            now_map[r][now] = now_map[r][c]
                            now_map[r][c] = 0
                        else:
                            if now_map[r][now] == now_map[r][c]:
                                now_map[r][now] *= 2
                                now_max_value = max(now_max_value, now_map[r][now])
                                now_map[r][c] = 0
                                now += di
                            else:
                                if c == now + di:
                                    now += di
                                else:
                                    now += di
                                    now_map[r][now] = now_map[r][c]
                                    now_map[r][c] = 0
        if now_max_value * (2 ** (4 - idx)) <= max_value:
            return
        idx += 1
    max_value = max(now_max_value, max_value)
    return


max_value = 0
dfs(0, '')
print(max_value)