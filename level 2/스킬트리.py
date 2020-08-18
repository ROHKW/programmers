# """
# 첫번째 루프에서 skill_trees에 담긴 요소를 하나씩 꺼내고, 선행 스킬이 필요한 스킬만을 담을 list 배열과 유효하지 않은 스킬트리를 체크하기 위한 fin을 True로 초기화한다.
# 두번째 루프에서 i[j]를 선행 스킬의 순서가 담겨있는 skill 배열과 비교하여 선행 스킬이 필요한 스킬만을 list 배열에 담는다.
# 생성한 list 배열의 길이 만큼 skill 배열과 같은 인덱스로 비교하여 값이 일치하지 않을 경우 fin을 False로 변경한다.
# fin이 True일 경우 유효한 스킬 트리이기 때문에 answer의 값에 1을 더해준 후 다시 루프를 반복한다.
# 해당 코드에서의 핵심은 선행 스킬이 필요한 스킬만을 담은 list 배열의 길이만큼 skill 배열과 비교하는 부분이다.
#
#
#
# 예를 들어 선행 스킬이 A-B-C의 순서라면 A를 먼저 배우지 않고서는 B와 C 스킬을 배울 수 없기 때문에 유효한 스킬트리라면 list 배열의 길이만큼 skill 배열과 같은 인덱스에서 같은 값을 가져야 하기 때문이다.
#
#
# """
# def solution(skill, skill_trees):
#     answer = 0
#
#     for i in skill_trees:
#         list = []
#         Test = True
#
#         for j in range(len(i)):
#             if i[j] in skill:
#                 list.append(i[j])
#
#         for k in range(len(list)):
#             if list[k] != skill[k]:
#                 Test = False
#                 break
#
#     if Test == True:
#         answer += 1
#
#     return answer
#


def solution(skill, skill_trees):
    answer = 0
    dic = dict()

    for i in range(len(skill)):
        dic[skill[i]] = i

    for i in range(len(skill_trees)):
        check = [-1]
        flag = True
        for j in range(len(skill_trees[i])):
            # 스킬순서에 있는거면
            if skill_trees[i][j] in dic:
                if check[len(check)-1] + 1 != dic[skill_trees[i][j]]:
                    flag = False
                    break
                check.append(dic[skill_trees[i][j]])

        if flag: answer += 1

    return answer

print(solution("ACD", ["ABCGEGEGWEGED"]))
