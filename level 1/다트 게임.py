def solution(dartResult):
    score = []
    answer = ''
    for shot in dartResult:
        if shot.isnumeric():
            answer += shot
        elif shot == 'S':
            score.append(int(answer) ** 1)
            answer = ''
        elif shot == 'D':
            score.append(int(answer) ** 2)
            answer = ''
        elif shot == 'T':
            score.append(int(answer) ** 3)
            answer = ''
        elif shot == '*':
            if len(score) > 1:
                score[-2] *= 2
            score[-1] *= 2
        elif shot == '#':
            score[-1] *= -1

    return sum(score)