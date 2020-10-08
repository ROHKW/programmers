
# dfs -> 스택, 재귀함수 이용
# 1. 탐색 시작 노드를 스택에 삽입 , 방문 처리
# 2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 하나라도 있으면, 그 노드를 스택에 넣고 방문처리,
# 방문하지 않은 인접 노드가 없다면(그 깊이탐색에 더이상 방문 안한 곳이 없다면?) 스택에 최상단 노드 꺼냄
# 3. 더이상 2번 과정 수행이 불가능 할때까지 반복




#####################################################################################
# 문제 풀이
# 얼음 0
# 벽 1
# 얼음 틀의 모양이 주어져 있을때 생성되는 총 아이스크림 개수 구하기

# N, M을 공백을 기준으로 구분하여 입력 받기
# dfs 사용하여 다음으로 진행
# 1. 특정지점의 주변 상 하 좌 우를 살펴본뒤 주변지점중에서 값이 0이면 아직 방문하지 않은 지점이 있다면 해당지점을 방문 한다
# 2. 방문한 지점에서 다시 상 하 좌 우를 살펴보면서 방문을 진행 하는 과정을 반복하며느 연결된 모든지점 방문 가능
# 3. 모든 노드에 대하여 1-2 반복 수행 , 방문하지 않은 지점수 카운트


import sys
n, m = map(int,sys.stdin.readline().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline())))


result = 0
for i in range(n):
    for j in range(m):

        if dfs(i , j) == True:
            result += 1

print(result)

def dfs(x, y):
    if x <= -1 or x >= n or y<=-1 or y>= m: # 이전부터 계속 실수하는 부분, 범위 벗어나는 값에 대한 처리
        return False


    if graph[x][y] == 0 :
        graph[x][y] ==1
        dfs(x-1, y)
        dfs(x, y -1)
        dfs(x+1, y)
        dfs(x, y+1)

        return True

    return False







