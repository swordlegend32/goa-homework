import random
List = [random.randint(1,1000) for i in range(10)]

print(List)
def GetSum(SumList):       
    sum = 0
    for i in SumList:
        sum += i
    return sum

print(GetSum(List))