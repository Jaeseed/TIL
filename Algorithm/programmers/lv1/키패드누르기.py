def solution(numbers, hand):
    answer = ''
    location_list = [
        [3,1],
        [0,0],
        [0,1],
        [0,2],
        [1,0],
        [1,1],
        [1,2],
        [2,0],
        [2,1],
        [2,2],
    ]
    left = [3,0]
    right = [3,2]
    for n in numbers:
        if n in [1,4,7]:
            answer += 'L'
            left = location_list[n]
        elif n in [3,6,9]:
            answer += 'R'
            right = location_list[n]
        else:
            er, ec = location_list[n]
            lr, lc = left
            rr, rc = right
            if abs(lr - er) + abs(lc-ec) > abs(rr-er) + abs(rc-ec):
                answer += 'R'
                right = [er,ec]
            elif abs(lr - er) + abs(lc-ec) < abs(rr-er) + abs(rc-ec):
                answer += 'L'
                left = [er,ec]
            else:
                if hand == 'left':
                    answer += 'L'
                    left = [er,ec]
                else:
                    answer += 'R'
                    right = [er,ec]
    return answer

solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right')