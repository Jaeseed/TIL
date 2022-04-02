def solution(s):
    answer = 2e29
    length = len(s)
    for i in range(1, length + 1):
        total_str = ''
        now_idx = i
        past_str = s[:i]
        cnt = 1
        while now_idx < length:
            if past_str == s[now_idx:now_idx + i]:
                cnt += 1
            else:
                if cnt == 1:
                    total_str += past_str
                else:
                    total_str += str(cnt) + past_str
                past_str = s[now_idx:now_idx + i]
                cnt = 1
            now_idx += i
            if answer <= len(total_str):
                break
        if cnt == 1:
            total_str += past_str
        else:
            total_str += str(cnt) + past_str
        answer = min(answer, len(total_str))

    return answer

solution("abcabcdede")