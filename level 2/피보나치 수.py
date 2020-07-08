def solution(n):
    answer = []
    for i in range(0, n):
        if i < 2:
            answer.append(1)
        else:
            answer.append(answer[i - 2] + answer[i - 1])

    return answer[-1]


def solution(n):
    answer = []
    for i in range(0, n):
        if i < 2:
            answer.append(1)
        else:
            answer.append(answer[i - 2] + answer[i - 1])

    return answer[-1] % 1234567