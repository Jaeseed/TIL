def solution(n, results):
    # 중복 제거
    tmp = set(map(tuple,results))
    results = list(tmp)
    answer = 0
    # 내가 이긴 선수
    win_list = [set() for _ in range(n+1)]
    # 내가 진 선수
    lose_list = [set() for _ in range(n+1)]
    for winner, loser in results:
        win_list[winner].add(loser)
        lose_list[loser].add(winner)
    for now in range(1, n+1):
        for winner in lose_list[now]:
            win_list[winner].update(win_list[now])
        for loser in win_list[now]:
            lose_list[loser].update(lose_list[now])
    for i in range(1,n+1):
        if len(win_list[i]) + len(lose_list[i]) == n-1:
            answer += 1
    print(answer)
    return answer
solution(5, [[1,5], [2,5], [5,3], [5,4],[3,4]])