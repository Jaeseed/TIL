def solution(routes):
    answer = 1
    routes.sort(key=lambda x: x[1])
    exit_ = routes[0][1]
    for idx in range(1,len(routes)):
        entrance = routes[idx][0]
        if exit_ < entrance:
            exit_ = routes[idx][1]
            answer += 1
    return answer