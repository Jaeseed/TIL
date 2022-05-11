def check(num):
    for i in range(2, num // 2):
        if num % i == 0:
            return False
    return True


def dfs(nums, cnt, idx, total):
    global answer
    if cnt == 3:
        if check(total):
            answer += 1
        return
    for i in range(idx, len(nums)):
        dfs(nums, cnt + 1, i + 1, total + nums[i])


def solution(nums):
    global answer
    answer = 0
    dfs(nums, 0, 0, 0)
    return answer
