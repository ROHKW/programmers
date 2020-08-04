import heapq


def solution(stock, dates, supplies, k):
    answer = 0
    day = 0
    flour = []

    while k > stock:
        for i in range(day, len(dates)):
            if dates[i] <= stock:  # i 번째 공급 가능일
                heapq.heappush(flour, -supplies[i])
            else:
                day = i
                break

        answer += 1
        stock -= heapq.heappop(flour)

    return answer
# 가동중지?


print(solution(4,[1,2,3,4], [10, 40, 20, 30], 100))