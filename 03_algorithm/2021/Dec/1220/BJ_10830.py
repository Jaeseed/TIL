N, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
binary_B = []
while B > 0:
    if B % 2:
        binary_B.append(1)
    else:
        binary_B.append(0)
    B //= 2
tmp_matrix = [[0] * N for _ in range(N)]
ans_matrix = [[0] * N for _ in range(N)]
flag = 0

for b in range(len(binary_B)):
    if binary_B[b] == 1:
        if flag == 0:
            for r in range(N):
                for c in range(N):
                    ans_matrix[r][c] = matrix[r][c] % 1000
            flag = 1
        else:
            for r in range(N):
                for n in range(N):
                    value = 0
                    for c in range(N):
                        value += ans_matrix[r][c] * matrix[c][n]
                    tmp_matrix[r][n] = value % 1000
            for r in range(N):
                for c in range(N):
                    ans_matrix[r][c] = tmp_matrix[r][c]
    if b == len(binary_B)-1:
        break
    for r in range(N):
        for n in range(N):
            value = 0
            for c in range(N):
                value += matrix[r][c] * matrix[c][n]
            tmp_matrix[r][n] = value % 1000
    for r in range(N):
        for c in range(N):
            matrix[r][c] = tmp_matrix[r][c]

for n in range(N):
    print(' '.join(map(str,ans_matrix[n])))