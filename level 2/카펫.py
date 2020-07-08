def solution(brown, yellow):
   for index in range(1,yellow+1):
        if yellow%index == 0:
            length = yellow//index
            if (((index+2)*(length+2))-(index*length)) == brown:
                return [max(index+2,length+2),min(index+2,length+2)]

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
