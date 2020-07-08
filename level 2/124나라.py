# def solution(n):
#     answer = ''
#     while n:
#         n, r = divmod(n, 3)
#         answer = "412"[r] + answer
#         if r == 0:
#             n -= 1
#     return answer
#



def solution(n):
    answer = ''
    while n > 0:
        n -= 1
        answer = '124'[n%3] + answer
        n //= 3
    return answer
print(solution(7))