# def solution(board):
#     for i in range(1, len(board)):
#         for j in range(1, len(board[0]):
#             if board[i][j] = 1:
#                 board[i][j] = min(board[i - 1][j], board[i][j - 1], board[i - 1][j - 1])
# 1 1
# 1 1  찾아서 계산
#     return max(
#

# 여기까지가 내 한계
# 아래 답 보고 푼거

from itertools import chain


def solution(board):
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            mins = min(board[i - 1][j - 1], board[i - 1][j], board[i][j - 1])
            if board[i][j] == 0 or mins == 0:
                continue
    #         board[i][j] = max(mins + 1, board[i][j])
    #
    # return max(list(chain.from_iterable(board))) ** 2
            else:
                if board[i-1][j] > 0 and board[i][j-1] > 0:
                    board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1
                if maxSquare < board[i][j]:
                    maxSquare = board[i][j]
    return maxSquare ** 2
print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))