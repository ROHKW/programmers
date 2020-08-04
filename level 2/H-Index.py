def solution(citations):
    answer = len(citations)
    citations.sort()

    while 1:  # 루프
        cnt = 0
        for i in citations:

            if i >= answer:
                cnt += 1
            if answer <= cnt:
                return answer
        answer -= 1

    return answer


print(solution([3, 5, 5, 5, 5]))
