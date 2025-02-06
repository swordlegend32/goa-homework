import random
import time

StudentsToGroup = [i for i in range(50)]

def GetGroups(Students):
    Groups = []
    NumberOfGroups = 0
    MinGroups = 1
    HighestStudentsPerGroup = 0
    ClosestDifference = float('inf')

    for i in range(MinGroups, 9999):
        StudentsPerGroup = len(Students) / i
        Difference = abs(StudentsPerGroup - i)
        if Difference != int(Difference):
            continue
        if Difference < ClosestDifference:
            ClosestDifference = Difference
            HighestStudentsPerGroup = StudentsPerGroup
            NumberOfGroups = i

    print(f"ჯგუფების რაოდენობა: {NumberOfGroups}")
    print(f"მოსწავლე ყოველ ჯგუფში: {HighestStudentsPerGroup}")

    Counting = (5,4,3,2,1)
    
    for i in Counting:
        print(f"Starting in {i}")
        time.sleep(1)

    for i in range(NumberOfGroups):
        Groups.append([])

    Index = 0

    while len(Students) > 0:
        Random = random.choice(Students)
        print(f"ვირჩევთ {Random} ჯგუფი {Index + 1} სთვის")
        Groups[Index].append(Random)
        Students.remove(Random)
        Index += 1
        if Index == NumberOfGroups:
            Index = 0
        time.sleep(0.5)

    return Groups

Grouped = GetGroups(StudentsToGroup)

for i in range(len(Grouped)):
    print(f"ჯგუფი {i + 1}: {Grouped[i]}")