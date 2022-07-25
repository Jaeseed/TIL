operation = input()
num = ''
num_list = []
operational_sign = []
idx = 0
while idx < len(operation):
    if 48 <= ord(operation[idx]) <= 57:
        num += operation[idx]
    else:
        num_list.append(int(num))
        num = ''
        operational_sign.append(operation[idx])
    idx += 1
num_list.append(int(num))
answer = num_list[0]
idx = 0
while idx < len(operational_sign):
    if operational_sign[idx] == '+':
        answer += num_list[idx + 1]
    else:
        tmp = num_list[idx + 1]
        idx += 1
        while idx < len(operational_sign) and operational_sign[idx] == '+':
            tmp += num_list[idx + 1]
            idx += 1
        answer -= tmp
        idx -= 1
    idx += 1
print(answer)