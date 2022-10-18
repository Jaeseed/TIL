def solution(dartResult):
    answer = 0
    calculation = []
    idx = 0
    while idx < len(dartResult):
        result = dartResult[idx]
        if 48 <= ord(result) <= 57:
            if result == '1':
                if dartResult[idx+1] == '0':
                    calculation.append(10)
                    idx += 2
                    continue
            calculation.append(int(result))
        elif result == 'D':
            calculation[-1] **= 2
        elif result == 'T':
            calculation[-1] **= 3
        elif result == '*':
            if len(calculation) > 1:
                calculation[-1] *= 2
                calculation[-2] *= 2
            else:
                calculation[-1] *= 2
        elif result == '#':
            calculation[-1] *= -1
        idx += 1
    for cal in calculation:
        answer += cal
    return answer