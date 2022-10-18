import sys
N, M = int(input()), int(input())
INF = 2e29
adj = [[INF] * (N+1) for _ in range(N+1)]
for m in range(M):
    st, en, ti = map(int,sys.stdin.readline().split())
    adj[st][en] = min(adj[st][en], ti)

# 경로 저장 리스트
route = [[[] for _ in range(N+1)] for __ in range(N+1)]

# 출발, 도착지가 같은 경로 모두 0처리
for n in range(1, N+1):
    adj[n][n] = 0

# 플로이드 워셜
for mid in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if adj[i][mid] + adj[mid][j] < adj[i][j]:
                adj[i][j] = adj[i][mid] + adj[mid][j]
                # 루트 초기화
                route[i][j] = []
                # 루트 갱신
                route[i][j] += route[i][mid] + [mid] + route[mid][j]

# INF 모두 0처리
for i in range(1, N+1):
    for j in range(1, N+1):
        if adj[i][j] == INF:
            adj[i][j] = 0
for n in range(1, N+1):
    print(' '.join(map(str,adj[n][1:])))

# 두번째 답 출력
for i in range(1, N+1):
    for j in range(1, N+1):
        if adj[i][j] == 0:
            print(0)
        else:
            # [길이, 경로]
            answer = [len(route[i][j])+2, i]
            answer += route[i][j]
            answer += [j]
            print(' '.join(map(str,answer)))