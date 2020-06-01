def solution(priorities, location):
    answer = []
    new_priorities = priorities[location]

    # print(new_priorities)
    while len(priorities) != 0:
        if priorities[0] < max(priorities):
            priorities.append(priorities.pop(0))
        else:
            answer.append(priorities.pop(0))


    return answer.index(new_priorities) + 1