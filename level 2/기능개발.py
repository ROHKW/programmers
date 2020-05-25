def solution(progresses, speeds):
    answer = [] # 빈 배열 <- 여따가 카운트된거 삽입
    # while:문을 돌리면서 'progresses'의 각 요소에 'speeds'의 각 요소를 더해줌
    while len(progresses):
        count = 0
        completed = False # 불린으로 작업 완료 구분
        for pgs in range(len(progresses)):
            progresses[pgs] += speeds[pgs]
        while len(progresses) != 0 and progresses[0] >= 100:
            count += 1
            completed = True
            progresses.pop(0)
            speeds.pop(0)
        if completed == True:
            answer.append(count)

    return answer

print(solution([93,30,55],[1,30,5]))