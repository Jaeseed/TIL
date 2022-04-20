def solution(w,h):
    W, H = w, h
    while H:
        W, H = H, W % H
    answer = w * h - (w + h - W)
    return answer