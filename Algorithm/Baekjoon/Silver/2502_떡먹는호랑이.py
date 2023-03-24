def fibonacci(a, b, step):
    if step == D:
        find(a, b)
        return
    fibonacci(b, a + b, step + 1)
    return


def find(a, b):
    global first, second
    tmp = 1
    while True:
        if (K - tmp * a) % b == 0:
            break
        tmp += 1
    first = tmp
    second = (K - tmp * a) // b
    return


D, K = map(int, input().split())
first = 0
second = 0
fibonacci(1, 1, 3)
print(f'{first}\n{second}')