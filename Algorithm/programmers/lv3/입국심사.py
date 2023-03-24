def solution(n, times):
    answer = 0
    min_time = min(times) * (n // len(times))
    max_time = max(max(times), min(times) * (n+1-len(times)))
    while min_time < max_time:
        cnt = 0
        mid = (max_time + min_time) // 2
        for time in times:
            cnt += mid // time
        if cnt >= n:
            max_time = mid
        else:
            min_time = mid + 1
    print(max_time)
    return answer
solution(6, [7,10])