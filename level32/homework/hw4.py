
List = [i for i in range(100)]

def GetMax(List):
    Highest = 0
    for i in List:
        if i > Highest:
            Highest = i
    return Highest

print(GetMax(List))