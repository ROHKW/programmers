answer = 0
def dfs(numbers, target, length, i):
    global answer
    if i == len(numbers):
        if (sum(numbers)) == target:
            answer += 1
            return
    else:
        dfs(numbers, target, length, i+1)
        numbers[i] *= -1
        dfs(numbers, target, length, i+1)


def solution(numbers, target):
    global answer
    length = len(numbers)
    dfs(numbers, target, length, 0)

    return answer

print(solution([1,1,1,1,1],3))