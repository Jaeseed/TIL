import sys
sys.setrecursionlimit(10 ** 9)

def search(now, target):
    global left, right
    if target < now:
        if left[now]:
            search(left[now], target)
        else:
            left[now] = target
    else:
        if right[now]:
            search(right[now], target)
        else:
            right[now] = target
    return


def post_order(now):
    if left[now]:
        post_order(left[now])
    if right[now]:
        post_order(right[now])
    print(now)
    return


input_value = sys.stdin.readline
input_list = []
left = [0] * 1000001
right = [0] * 1000001
flag = 1
# try:
#     while True:
#         tmp = int(input_value())
#         if flag == 1:
#             root = tmp
#             flag = 0
#             continue
#         search(root, tmp)
# except:
#     post_order(root)
#     exit()




input_list = range(1,10000)
root = 1
for i in range(1, len(input_list)):
    if i % 1290 == 0:
        print(3)
    search(root, input_list[i])
post_order(1)