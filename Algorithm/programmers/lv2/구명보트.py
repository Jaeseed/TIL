def solution(people, limit):
    answer = 0
    people.sort()
    start = len(people) - 1
    end = 0
    while start > end:
        high = people[start]
        low = people[end]
        if high + low <= limit:
            start -= 1
            end += 1
        else:
            start -= 1
        answer += 1
    if start == end:
        answer += 1
    return answer