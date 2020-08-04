def solution(people, limit):
    answer = 0
    people.sort()
    LW = 0 # 가벼운 찬구 Light Weight
    HW = len(people)-1 # 무거운 친구 Heavy Weight

# 무거운 친구를 기준으로 작은애들 1+1 했을때 limit에 걸리는지?
# if 문에서 인덱스 카운트 하고 len(people)에서 빼기
    while LW < HW:
        if people[LW] + people[HW] <= limit:
            answer += 1
            LW += 1
            HW -= 1
        else:
            HW -= 1
        # answer += 1

    return len(people) - answer

print(solution([70, 80,25,30,95,40,75,66,50, 80],100))
