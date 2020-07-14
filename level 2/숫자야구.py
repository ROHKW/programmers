# * 숫자는 맞지만, 위치가 틀렸을 때는 볼
# * 숫자와 위치가 모두 맞을 때는 스트라이크
# * 숫자와 위치가 모두 틀렸을 때는 아웃
# 순열개념 필요? print(list(itertools.permutations())

from itertools import permutations

def solution(baseball):
    # 모든 경우 순열로 받아옴
    numbers=list(range(1,10))
    num_list = list(permutations(numbers,3))
    # 스트라이크(s)와 볼(b)
    s, b = 0, 0
    copy = list(num_list)  # 반복문을 돌며 하나씩 리스트의 값을 제거하기 때문에 복사
    for i in range(len(baseball)):  # 시도한 횟수
        trial = str(baseball[i][0])  # 시도할 때의 숫자를 문자형으로 치환
        for j in num_list:  # 모든 경우의 수
            for k in range(3):  # 총 세자리 숫자이므로 세번 반복
                if int(trial[k]) == j[k]:  # 위치가 동일= 스트라이크 += 1
                    s += 1
                if int(trial[k]) in j:  # 값이 있다= 볼 += 1
                    b += 1
            # 현재 체크하고 있는 값이 s와 b가 일치하지 않는다면
            if not(s == baseball[i][1] and b == baseball[i][1] + baseball[i][2]):
                if j in copy:  # 그리고 copy안에 현재 체크하고 있는 값이 있다면
                    copy.remove(j)  # copy리스트에서 현재 체크하고 있는 값을 제거
            s, b = 0, 0  # 현재 값에대한 스트라이크와 볼 초기화
    return len(copy)  # 남은 copy 리턴(가능한 정답의 수)

print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))


