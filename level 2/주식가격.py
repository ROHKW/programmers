from collections import deque


def solution(prices):
    answer = []
    prices = deque(prices)
    price = len(prices)
    while price != 0:
        temp = prices.popleft()
        price -= 1
        adding = 0
        for i in range(price):
            if temp > prices[i]:
                adding += 1
                break
            else:
                adding += 1
        answer.append(adding)
    return answer


print(solution([1, 2, 3,2,3]))
