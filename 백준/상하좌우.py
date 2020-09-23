import sys
x, y = 1, 1

def direction():

    N = int(sys.stdin.readline())
    Plan = list(sys.stdin.readline().split())

    x = 1
    y = 1

    for i in range(len(Plan)):

        if Plan[i] == 'L'and y > 1:
            y -= 1

        elif Plan[i] == 'R' and y < N:
            y += 1

        elif Plan[i] =='U' and x > 1:
            x -= 1

        elif Plan[i] == 'D' and x < N :
            x += 1

    print(x, y)


