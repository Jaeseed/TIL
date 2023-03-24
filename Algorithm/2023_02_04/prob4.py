def solution(n, m, p):
    answer = 0
    a_people, a_eat = n, m
    b_people, b_eat = 0, 0
    # 정원이 1명이거나 사람 수가 식인종 수보다 적으면 -1 return
    if p == 1 or n < m:
        return -1
    # 사람 수와 식인종 수가 같고 정원과 다르면 -1 return
    if n == m and m > p:
        return -1
    if n == m == p:
        return 5
    while True:
        new_p = p // 2
        if p % 2:
            new_p += 1
            if a_people == a_eat:
                new_p -= 1
        if a_eat == 0:
            a_people -= p
            b_people += p
        elif a_eat < p // 2:
            a_people -= new_p+ a_eat
            b_people += new_p + a_eat
            b_eat += a_eat
            a_eat = 0
        else:
            a_people -= new_p
            b_people += new_p
            a_eat -= p // 2
            b_eat += p // 2
        answer += 1
        if a_people + a_eat <= 0:
            break
        if a_eat > a_people or b_eat > b_people:
            return -1
        if b_people == b_eat:
            a_eat += 1
            b_eat -= 1
        else:
            a_people += 1
            b_people -= 1
        if a_eat > a_people or b_eat > b_people:
            return -1
    print(answer)
    return answer
solution(3,1,2)