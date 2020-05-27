import numpy as np

def solution(arr1, arr2):
    a1 = np.array(arr1)
    a2 = np.array(arr2)
    print('a1', a1)
    print('a2', a2)
    answer = a1 + a2
    print(answer)
    solution = answer.tolist()
    return solution


print(solution([[1,2],[2,3]],[[3,4],[5,6]]))