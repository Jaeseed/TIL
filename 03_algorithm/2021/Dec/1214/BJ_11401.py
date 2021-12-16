import time
N, K = map(int,input().split())
start = time.time()
# value = 1
# if N-K < N // 2:
#     for n in range(N, K, -1):
#         value *= n
#     for k in range(1, N-K+1):
#         value //= k
#     ans = value % 1000000007
# else:
#     for n in range(N, N-K, -1):
#         value *= n
#     for k in range(1, K+1):
#         value //= k
#     ans = value % 1000000007
for i in range(1000000):
    for j in range(1000000):
        a = 3
print("time: ", time.time() - start)
# print(value)
# print(ans)