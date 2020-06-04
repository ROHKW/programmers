def solution(arrangement):
    lazerarrangement = list(arrangement.replace("()","L"))
    answer = 0
    x = 0
    count = 0
    for i in lazerarrangement:
        if i == "(":
            x += 1
        elif i == "L":
            answer += x
        elif i == ")":
            x -= 1
            count += 1
    answer += count
    return answer

print(solution("()(((()())(())()))(())"))