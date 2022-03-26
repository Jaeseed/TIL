def solution(new_id):
    answer = ''
    before = ''
    now = ''
    all_special_cha = '~!@#$%^&*()=+[{]}:?,<>/'
    for n in range(len(new_id)):
        if len(answer) == 15:
            break
        now = new_id[n]
        if now == '.':
            if len(answer) == 0 or before == '.':
                continue
        if now in all_special_cha: continue
        if ord('A') <= ord(now) <= ord('Z'):
            answer += chr(ord(now)+32)
        elif now == ' ':
            answer += 'a'
        else:
            answer += now
        before = now
    if answer and answer[-1] == '.':
        answer = answer[:-1]
    if len(answer) < 1:
        answer = 'aaa'
    elif 1 <= len(answer) < 3:
        while len(answer) < 3:
            answer += answer[-1]
    return answer


solution("z-+.^.")