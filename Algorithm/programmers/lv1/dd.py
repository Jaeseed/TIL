import copy


def solution(n, costs):
    answer = 0
    MAP = [[0] * n for _ in range(n)]

    for s, e, cost in costs:
        MAP[s][e] = cost
        MAP[e][s] = cost
    floyd = copy.deepcopy(MAP)
    route = [[[] for _ in range(n)] for _ in range(n)]
    print(route)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if floyd[i][k] and floyd[k][j]:
                    if floyd[i][j] == 0:
                        floyd[i][j] = min(floyd[i][k], floyd[k][j])
                        route[i][j] = route[i][k] + [k] + route[k][j]
                    elif floyd[i][j]:
                        if floyd[i][j] > floyd[i][k] or floyd[i][j] > floyd[k][j]:
                            route[i][j] = route[i][k] + [k] + route[k][j]
    selected_route = []
    for i in range(1,n):
        past = i
        for j in route[0][i]:
            if [past,j] not in selected_route:
                selected_route.append([past,j])
            past = j
        if [past,j] not in selected_route:
            selected_route.update([past,i])
    print(selected_route)
    for r,c in selected_route:
        answer += MAP[r][c]
    return answer
solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])