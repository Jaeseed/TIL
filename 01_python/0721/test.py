# 1. 재귀함수 factorial

# def factorial(n):
#     if n == 1:
#         return n
#     else:
#         return n * factorial(n-1)
# print(factorial(8))


# 2. 재귀함수 피보나찌

# def fib(n):
#     if n < 2:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)


# print(fib(100))


# 3-1 반복문

def fib_for(n):
    if n < 2:
        return n
    
    a, b = 0, 1

    for i in range(n-1):
        a, b = b, a + b
    return b

print(fib_for(3))
