import sys
sys.setrecursionlimit(10000000)
def find_goal(adj,now_subway,end_subway,step,answer,visited):
    if step >= answer[0]:
        return
    for i in adj[now_subway]:
        if i == end_subway:
            if step < answer[0]:
                answer[0] = step
            return
        if visited[i] == 0:
            visited[i] = 1
            find_goal(adj,i,end_subway,step+1,answer,visited)
            visited[i] = 0
    return

def solution(subway, start, end):
    station = [[] for _ in range(1000001)]
    idx = 0
    for s in subway:
        list_ = list(map(int,s.split()))
        for l in list_:
            station[l].append(idx)
            if l == start:
                start_subway = idx
            if l == end:
                end_subway = idx
        idx += 1
    adj = [[] for _ in range(len(subway))]
    for st in range(1000001):
        if len(station[st]) > 1:
            for i in station[st]:
                for j in station[st]:
                    if i == j: continue
                    if j not in adj[i]:
                        adj[i].append(j)
    visited = [0] * len(subway)
    visited[start_subway] = 1
    answer = [2e29]
    if start_subway == end_subway:
        answer[0] = 0
    find_goal(adj,start_subway,end_subway,1,answer,visited)
    return answer[0]
solution(

["1 2 3 4 5 6 7 8", "2 11", "0 11 10", "3 17 19 12 13 9 14 15 10", "20 2 21"], 1, 9)