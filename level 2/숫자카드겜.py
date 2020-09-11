n = map(int, input().split())
m = map(int, input().split())

finalcard = []

for i in range(1,n+1):
    data = list(map(int, input().split()))
    Min = min(data)
    FinalCard = finalcard.append(Min)
    Max =  max(FinalCard)

print(Max)
