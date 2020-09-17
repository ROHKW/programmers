import sys

n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))

number = 0

s.sort()
for i in range(n):
    for j in range(i + 1):
        number += s[j]

print(number)