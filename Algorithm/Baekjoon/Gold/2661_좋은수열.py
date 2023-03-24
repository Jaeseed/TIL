def sequence(now, step, before):
    if step == N:
        return now
    for i in range(1, 4):
        if i == before: continue
        if check(now + str(i), step+1):
            ret = sequence(now + str(i), step + 1, i)
            if ret:
                return ret
    return ''


def check(now, step):
    for i in range(1, step // 2 + 1):
        cnt = 0
        for j in range(i):
            if now[step-1-j] == now[step-1-j-i]:
                cnt += 1
        if i == cnt:
            return False
    return True


N = int(input())
answer = sequence('', 0, 0)
print(answer)