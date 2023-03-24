def solution(info, query):
    answer = []
    # idx 분리 딕셔너리
    i_d = {
        'cpp': 0,
        'java': 1,
        'python': 2,
        'backend': 0,
        'frontend': 1,
        'junior': 0,
        'senior': 1,
        'chicken': 0,
        'pizza': 1,
    }
    # 경우의 수 별로 점수를 정리 -> 언어 - 직군 - 경력 - 소울푸드 - 점수
    all_info = [[[[[0] * 100001 for l in range(2)]for k in range(2)] for j in range(2)] for i in range(3)]
    # 쿼리에 맞게
    for unit in info:
        # 현재 info를 리스트로 변환
        ni = list(unit.split())
        all_info[i_d[ni[0]]][i_d[ni[1]]][i_d[ni[2]]][i_d[ni[3]]][int(ni[4])] += 1
    # 큰 점수를 가진 인원 수를 작은 수의 인원에 더함
    for i in range(3):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    for m in range(100001,0,-1):
                        all_info[i][j][k][l][m-1] += all_info[i][j][k][l][m]

    for q in query:
        nq = list(q.split())
        target = int(nq[-1])
        search = []
        if nq[0] == '-':
            search.append([0,1,2])
        else:
            search.append([i_d[nq[0]]])
        for i in range(2,7,2):
            if nq[i] == '-':
                search.append([0,1])
            else:
                search.append([i_d[nq[i]]])
        now_answer = 0
        for i in search[0]:
            for j in search[1]:
                for k in search[2]:
                    for l in search[3]:
                        now_answer += all_info[i][j][k][l][target]
        answer.append(now_answer)
    return answer

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])