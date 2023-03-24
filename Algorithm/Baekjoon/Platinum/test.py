def solution(K, user_scores):
    answer = 0
    arr = [['', 0] for _ in range(K)]
    user_dict = dict()
    for user_score in user_scores:
        tmp = list(user_score.split())
        name = tmp[0]
        score = int(tmp[1])
        if name in user_dict:
            if arr[user_dict[name]][1] >= score: continue
            start = user_dict[name]
        else:
            start = K - 1
        while start >= 0:
            if arr[start][1] >= score:
                break
            if arr[start][0] == '':
                start -= 1
                continue
            if start != K-1:
                if arr[start][0] == name:
                    arr[start] = ['',0]
                else:
                    arr[start+1][0],arr[start+1][1] = arr[start][0], arr[start][1]
                    if arr[start+1][0] in user_dict:
                        user_dict[arr[start+1][0]] = start + 1
            start -= 1
        if start + 1 == K: continue
        if name in user_dict and user_dict[name] == start + 1:
            pass
        else:
            answer += 1
        arr[start + 1] = [name,score]
        user_dict[name] = start + 1
    print(answer, arr)
    return answer


solution(
2, ["alex1 10", "alex11 100", "alex111 20", "alex1 30"])