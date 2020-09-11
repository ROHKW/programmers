n = map(int, input().split())
m = map(int, input().split())
k = map(int, input().split())


data  = list(map(int, input().split()))
data.sort(reverse = True)

first = data[0]
second = data[1]

result = (first*k*(m // (k+1)) + (m % (k+1))) + second*(m // (k+1))

print(result)
