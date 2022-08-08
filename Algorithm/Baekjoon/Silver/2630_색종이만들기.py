def divide(sr, sc, er, ec):
    if check_unity(sr,sc,er,ec):
        pass
    else:
        if er - sr == 1:
            check_unity(sr,sc,er,ec)
            return
        mean = (er - sr) // 2
        for r in range(2):
            for c in range(2):
                divide(sr + mean * r, sc + mean * c, sr + mean * (r + 1), sc + mean * (c + 1))
    return


def check_unity(sr,sc,er,ec):
    global blue_paper, white_paper
    standard = MAP[sr][sc]
    for r in range(sr,er):
        for c in range(sc,ec):
            if MAP[r][c] != standard:
                return False
    if standard == 1:
        blue_paper += 1
    else:
        white_paper += 1
    return True


N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
white_paper = 0
blue_paper = 0
divide(0, 0, N, N)
print(white_paper)
print(blue_paper)