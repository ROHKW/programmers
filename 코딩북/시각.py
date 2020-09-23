import sys
h = int(sys.stdin.readline())

count = 0

for i in range(h+ 1):
    for j in range(60):
        for a in range(60):
            if "3" in str(i) + str(j) + str(a):
                count +=1
# 다 델고와서 문자열로 만들고 그 중에 3이 있냐 없냐로 카운트 해주기?
print(count)