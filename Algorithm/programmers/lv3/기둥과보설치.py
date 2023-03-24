def check_column(y,x,column,beam):
    # 바닥일 때
    if y == 0:
        pass
    # 아래에 보가 있을 때
    elif (x > 0 and beam[y][x-1]) or beam[y][x]:
        pass
    # 아래에 기둥이 있을 때
    elif column[y-1][x]:
        pass
    else:
        return False
    return True


def check_beam(y,x,column,beam):
    if column[y-1][x] or column[y-1][x+1]:
        pass
    elif 0 < x and beam[y][x-1] and beam[y][x+1]:
        pass
    else:
        return False
    return True


def solution(n, build_frame):
    answer = []
    column = [[0] * (n+1) for _ in range(n+1)]
    beam = [[0] * (n+1) for _ in range(n+1)]
    for x, y, a, b in build_frame:
        # 설치
        if b == 1:
            # 기둥
            if a == 0:
                if check_column(y,x,column,beam):
                    column[y][x] = 1
            # 보
            else:
                # 조건 확인
                if check_beam(y,x,column,beam):
                    beam[y][x] = 1
        #삭제
        else:
            # 기둥
            if a == 0:
                column[y][x] = 0
                flag = 0
                # 위 기둥 검사
                if y < n and column[y+1][x] and not check_column(y+1,x,column,beam):
                    pass
                # 왼쪽 보 검사
                elif x > 0 and beam[y+1][x-1] and not check_beam(y+1,x-1,column,beam):
                    pass
                # 오른쪽 보 검사
                elif x < n and beam[y+1][x] and not check_beam(y+1,x,column,beam):
                    pass
                else:
                    flag = 1
                if flag == 0:
                    column[y][x] = 1
            # 보
            else:
                beam[y][x] = 0
                flag = 0
                # 왼쪽 기둥 검사
                if column[y][x] and not check_column(y,x,column,beam):
                    pass
                # 오른쪽 기둥 검사
                elif column[y][x+1] and not check_column(y,x+1,column,beam):
                    pass
                # 왼쪽 보 검사
                elif x > 0 and beam[y][x-1] and not check_beam(y,x-1,column,beam):
                    pass
                # 오른쪽 보 검사
                elif beam[y][x+1] and not check_beam(y,x+1,column,beam):
                    pass
                else:
                    flag = 1
                if flag == 0:
                    beam[y][x] = 1
    for c in range(n+1):
        for r in range(n+1):
            if column[r][c]:
                answer.append([c,r,0])
            if beam[r][c]:
                answer.append([c,r,1])
    return answer
solution(	5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]])