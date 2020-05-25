def solution(d, budget):
    answer = 0
    d.sort() # 정렬한번 해주고 ( 싼거 부터 사는 나쁜 예산 )
    for cost in d: # for문으로  해결하기
        budget -= cost
        answer += 1
        if budget < 0: # 예산을 초과하여 살순 없으니 빠꾸
            answer -=1
            break
    return answer