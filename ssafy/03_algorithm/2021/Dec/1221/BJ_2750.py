N = int(input())
arr = []
for n in range(N):
    unit = int(input())
    arr.append(unit)
arr.sort()
for n in range(N):
    print(arr[n])