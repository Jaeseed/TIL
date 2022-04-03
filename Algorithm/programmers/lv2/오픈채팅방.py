def solution(record):
    answer = []
    id_dict = dict()
    # 들어오는게 1, 나가는건 0
    log = []
    for rec in record:
        rec = list(rec.split())
        if rec[0] == 'Leave':
            log.append([rec[1], 0])
            pass
        else:
            user, nickname = rec[1], rec[2]
            id_dict[user] = nickname
            if rec[0] == 'Enter':
                log.append([user, 1])
    for user_, act in log:
        if act == 1:
            answer.append('{}님이 들어왔습니다.'.format(id_dict[user_]))
        else:
            answer.append('{}님이 나갔습니다.'.format(id_dict[user_]))
    print(answer)
    return answer


solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])