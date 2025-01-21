List = [i for i in range(100)]


def GetMin(List):
    Lowest = None
    for i in List:
        if not Lowest:
            Lowest = i
            continue
        if i < Lowest:
            Lowest = i
    return Lowest

print(GetMin(List))