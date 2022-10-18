import math
def is_prime_num(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True
def solution(n, k):
    new_num = ''
    while n:
        if n % k:
            new_num += str(n%k)
        else:
            new_num += '0'
        n //= k
    new_num = new_num[::-1]
    answer = 0
    candidate = ''
    for unit in new_num:
        if unit != '0':
            candidate += unit
        elif unit == '0' and candidate:
            if is_prime_num(int(candidate)):
                answer += 1
            candidate = ''
    if candidate:
        if is_prime_num(int(candidate)):
            answer += 1
    return answer