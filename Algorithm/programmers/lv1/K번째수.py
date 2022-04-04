def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        tmp = array[i-1:j]
        tmp.sort()
        answer.append(tmp[k-1])
    print(answer)
    return answer

solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]])