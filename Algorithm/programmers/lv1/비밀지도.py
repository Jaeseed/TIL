def solution(n, arr1, arr2):
    answer = []
    MAP1 = [[0] * n for _ in range(n)]
    MAP2 = [[0] * n for _ in range(n)]
    for i in range(n):
        now = arr1[i]
        jump = -1
        while now:
            if now % 2:
                MAP1[i][jump] = 1
            now //= 2
            jump -= 1
    for i in range(n):
        now = arr2[i]
        jump = -1
        while now:
            if now % 2:
                MAP2[i][jump] = 1
            now //= 2
            jump -= 1
    for i in range(n):
        this_row = ''
        for j in range(n):
            if MAP1[i][j] or MAP2[i][j]:
                this_row += '#'
            else:
                this_row += ' '
        answer.append(this_row)
    return answer