def solution(s):
    answer = 0
    num_dict = {
        'zero': 0,
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    str_answer = ''
    tong = ''
    for i in s:
        if ord('0') <= ord(i) <= ord('9'):
            str_answer += i
        else:
            tong += i
            if tong in num_dict:
                str_answer += num_dict[tong]
                tong = ''
    if str_answer:
        answer = int(str_answer)
    print(answer)
    return answer
solution('')