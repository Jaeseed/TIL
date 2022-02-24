# path = [
#     [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],
#     [10, 13, 16, 19, 25, 30, 35, 40],
#     [20, 22, 24, 25, 30, 35, 40],
#     [30, 28, 27, 26, 25, 30, 35, 40],
#     [25, 30, 35, 40]
# ]
#
#
# def dfs(step, str_):
#     if step == 10:
#         score(str_)
#         return
#     for i in range(1, 5):
#         dfs(step + 1, str_ + str(i))
#     return
#
#
# def score(str_):
#     global ans
#     complete_list = []
#     # if str_ == '1122122222':
#     #     print(3)
#     spot_list = [[0, 0] for _ in range(5)]
#     map_ = [[0] * 22 for _ in range(4)]
#     triangle_zone = [0, 0, 0, 0]
#     total = 0
#     for i in range(10):
#         target, move = int(str_[i]), A[i]
#         if target in complete_list: return
#         post_path, post_idx = spot_list[target]
#         post_value = path[post_path][post_idx]
#         map_[post_path][post_idx] = 0
#         tf = 25
#         for j in range(4):
#             if post_value == 30 and post_path == 0: break
#             if post_value == tf + j * 5:
#                 triangle_zone[j] = 0
#         if post_idx + move >= len(path[post_path]):
#             complete_list.append(target)
#             map_[post_path][post_idx] = 0
#             continue
#         if post_value == 10:
#             spot_list[target] = [1, 0]
#         elif post_value == 20:
#             spot_list[target] = [2, 0]
#         elif post_value == 30 and post_path == 0:
#             spot_list[target] = [3, 0]
#         now_path, now_idx = spot_list[target]
#         now_idx += move
#         now_value = path[now_path][now_idx]
#
#         for j in range(4):
#             if now_value == 30 and now_path == 0: break
#             if now_value == tf + j * 5:
#                 if triangle_zone[j] == 1:
#                     return
#                 else:
#                     triangle_zone[j] = 1
#         if map_[now_path][now_idx]:
#             return
#         total += now_value
#         map_[now_path][now_idx] = 1
#         spot_list[target] = [now_path, now_idx]
#     ans = max(ans, total)
#     # if total == 222:
#     #     print(3)
#     return
#
#
# A = list(map(int, input().split()))
# ans = 0
# dfs(0, '')
# print(ans)

import sys

input = sys.stdin.readline

a = [0 for _ in range(33)]
for i in range(21):
    a[i] = i+1
a[21] = 21
a[22], a[23], a[24] = 23, 24, 30
a[25], a[26] = 26, 30
a[27], a[28], a[29] = 28, 29, 30
a[30], a[31], a[32] = 31, 32, 20

move_in = [0 for _ in range(16)]
move_in[5], move_in[10], move_in[15] = 22, 25, 27

plus = [0 for _ in range(33)]
for i in range(1, 21):
    plus[i] = i * 2
plus[22], plus[23], plus[24] = 13, 16, 19
plus[25], plus[26] = 22, 24
plus[27], plus[28], plus[29] = 28, 27, 26
plus[30], plus[31], plus[32] = 25, 30, 35

def dfs(dice_index, ans, str_):
    global max_ans
    if dice_index == 10:
        max_ans = max(max_ans, ans)
        if ans == 231:
            print(str_)
        return

    for i in range(4):
        x, x0, move = chess[i], chess[i], dice[dice_index]

        if x == 5 or x == 10 or x == 15:
            x = move_in[x]
            move -= 1

        if x + move <= 21:
            x += move
        else:
            for _ in range(move):
                x = a[x]

        if c[x] and x != 21:
            continue

        c[x0], c[x], chess[i] = 0, 1, x
        dfs(dice_index + 1, ans + plus[x], str_ + str(i))
        c[x0], c[x], chess[i] = 1, 0, x0

dice = list(map(int, input().split()))
chess = [0 for _ in range(4)]
c = [0 for _ in range(33)]

max_ans = 0
dfs(0, 0, '')
print(max_ans)