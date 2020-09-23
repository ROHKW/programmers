import sys
h = int(sys.stdin.readline())

count = 0

for i in range(h+ 1):
    for j in range(60):
        for a in range(60):
            if "3" in str(i) + str(j) + str(a):
                count +=1

print(count)