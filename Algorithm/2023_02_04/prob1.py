def make_except(weight, cnt, idx, past, step, max_weight):
    if step == cnt:
        all_players = ''
        for j in range(len(weight)):
            if str(j) not in idx:
                all_players += str(j)
        max_weight = divide_team(all_players, '', weight, max_weight,0)
        return max_weight
    for i in range(past, len(weight)):
        max_weight = make_except(weight, cnt, idx + str(i), i+1, step + 1, max_weight)
        max_weight = make_except(weight, cnt, idx, i+1, step + 1, max_weight)
    return max_weight


def divide_team(all_players, now_players, weight, max_weight, past):
    if now_players:
        a_team = 0
        b_team = 0
        for player in all_players:
            if player in now_players:
                a_team += weight[int(player)]
            else:
                b_team += weight[int(player)]
        if a_team == b_team:
            max_weight = max(max_weight, a_team)
    for i in range(past, len(all_players)):
        max_weight = divide_team(all_players, now_players + all_players[i], weight, max_weight, i+1)
        max_weight = divide_team(all_players, now_players, weight, max_weight, i+1)
    return max_weight


def solution(weight):
    answer = []
    max_weight = 0
    max_weight = make_except(weight, 0, '', 0, 0, max_weight)
    if max_weight:
        answer = [len(weight), max_weight]
        print(answer)
        return answer
    for i in range(1, len(weight) - 1):
        max_weight = make_except(weight, i, '', 0, 0, max_weight)
        if max_weight:
            answer = [len(weight) - i, max_weight]
            print(answer)
            return answer
    print(answer)
    return answer
solution(
[40,30])