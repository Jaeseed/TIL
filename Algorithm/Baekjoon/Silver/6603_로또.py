def recursion(idx, step, nums):
    if step == 6:
        print(' '.join(map(str,nums)))
        return
    for i in range(idx, len(lotto)):
        recursion(i + 1, step + 1, nums + [lotto[i]])


while True:
    tmp = input()
    if len(tmp) == 1:
        break
    input_list = list(map(int, tmp.split()))
    S = input_list[0]
    lotto = input_list[1:]
    recursion(0, 0, [])
    print()
