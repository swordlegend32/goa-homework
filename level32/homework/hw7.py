
List = [i for i in range(10)]
OddList = [i for i in List if i % 2 != 0]
SumList = [0]

for i in OddList:
    SumList[0] += i

for i in range(10):
    print(SumList)