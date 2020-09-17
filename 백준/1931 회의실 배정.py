import sys

N = int(sys.stdin.readline())
meeting = []

for _ in range(N):
    a, z = map(int, sys.stdin.readline().split())
    meeting.append((a, z))

meeting = sorted(meeting, key=lambda x: (x[1], x[0]))

count = 1

previous = meeting[0][1]

for Next in meeting[1:]:
    if previous <= Next[0]:
        previous = Next[1]
        count += 1
print(count)



