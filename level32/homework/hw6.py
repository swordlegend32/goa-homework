
List = [i for i in range(10)]
EvenList = [i for i in List if i % 2 == 0]
SumList = [0]

for i in EvenList:
    SumList[0] += i

for i in range(10):
    print(SumList)