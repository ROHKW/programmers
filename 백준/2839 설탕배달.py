N = int(input())
Box = 0
while True:
    if (N % 5) == 0:
        Box = Box + (N //5)
        print(Box)
        break

    N -= 3
    Box += 1
    if N < 0:
        print('-1')
        break


