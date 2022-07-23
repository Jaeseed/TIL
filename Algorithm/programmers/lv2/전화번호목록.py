def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(1, len(phone_book)):
        before = phone_book[i-1]
        now = phone_book[i]
        flag = 1
        for j in range(len(before)):
            if before[j] != now[j]:
                flag = 0
                break
        if flag == 1:
            answer = False
            break
    return answer