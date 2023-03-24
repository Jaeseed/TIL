N, M, R = map(int,input().split())
items = [0] + list(map(int,input().split()))
INF = 2e29
MAP = [[INF] * (N+1) for _ in range(N+1)]
for i in range(R):
    a, b, l = map(int, input().split())
    MAP[a][b], MAP[b][a] = min(MAP[a][b],l), min(MAP[b][a],l)

# 중간 노드
for m in range(1, N+1):
    # 시작 노드
    for s in range(1, N+1):
        # 도착 노드
        for e in range(1, N+1):
            if s == e: continue
            MAP[s][e] = min(MAP[s][e], MAP[s][m] + MAP[m][e])
answer = 0
for r in range(1, N+1):
    now = items[r]
    for c in range(1, N+1):
        if MAP[r][c] <= M:
            now += items[c]
    answer = max(answer, now)
print(answer)