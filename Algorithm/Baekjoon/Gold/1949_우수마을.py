import sys

sys.setrecursionlimit(10 ** 6)


def choose(now, prev):
    use_me = resident[now]
    not_use_me = 0
    for node in adj[now]:
        if node == prev: continue
        use_son, not_use_son = choose(node, now)
        use_me += not_use_son
        not_use_me += max(use_son, not_use_son)
    return use_me, not_use_me


N = int(input())
resident = list(map(int, input().split()))
adj = [[] for _ in range(N)]
for n in range(N - 1):
    v1, v2 = map(int, sys.stdin.readline().split())
    adj[v1 - 1].append(v2 - 1)
    adj[v2 - 1].append(v1 - 1)
print(max(choose(0, -1)))
