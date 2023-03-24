def solution(board, skill):
    answer = 0
    N = len(board)
    M = len(board[0])
    stacked_map = [[0] * (M + 1) for _ in range(N+1)]
    for t, r1, c1, r2, c2, d in skill:
        if t == 1:
            d *= -1
        stacked_map[r1][c1] += d
        stacked_map[r1][c2+1] += -d
        stacked_map[r2+1][c1] += -d
        stacked_map[r2+1][c2+1] += d
    for r in range(N):
        for c in range(M):
            stacked_map[r][c+1] += stacked_map[r][c]
    for c in range(M):
        for r in range(N):
            stacked_map[r+1][c] += stacked_map[r][c]
            if board[r][c] + stacked_map[r][c] > 0:
                answer += 1
    return answer
solution(	[[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]], [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]])