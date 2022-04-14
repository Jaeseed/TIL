def solution(board, moves):
    answer = 0
    tong = [0]
    for move in moves:
        for r in range(len(board)):
            if board[r][move-1]:
                now = board[r][move-1]
                board[r][move-1] = 0
                if tong[-1] == now:
                    tong.pop()
                    answer += 2
                else:
                    tong.append(now)
                break
    return answer

    return answer

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])