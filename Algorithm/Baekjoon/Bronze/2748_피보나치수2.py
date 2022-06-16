N = int(input())
pib = [0, 1]
n = 2
while n <= N:
    tmp = pib[n-2] + pib[n-1]
    pib.append(tmp)
    n += 1
print(pib[-1])

