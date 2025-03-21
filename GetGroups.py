import random
import time
import math

# random.seed(3)

StudentsToGroup = [i for i in range(50)]

def GetGroups(Students):
    Groups = []
    AllStudents = []
    NumberOfGroups = 0
    MinGroups = 1
    StudentsPerGroup = 3

    for i in range(MinGroups, 9999):
        NumberOfGroups =  math.ceil(len(Students) / StudentsPerGroup)

    print(f"ჯგუფების რაოდენობა: {NumberOfGroups}")
    print(f"მოსწავლე ყოველ ჯგუფში: {StudentsPerGroup}")

    Counting = (5,4,3,2,1)
    
    for i in Counting:
        print(f"Starting in {i}")
        time.sleep(1)

    for i in range(NumberOfGroups):
        Groups.append([])

    if "გიორგი თედოზაშვილი" in Students and "ნიკა დობო" in Students:
        Students.remove("გიორგი თედოზაშვილი")
        Students.remove("ნიკა დობო")
        
        for group in Groups:
            if len(group) + 2 <= StudentsPerGroup:
                group.append("გიორგი თედოზაშვილი")
                group.append("ნიკა დობო")
                AllStudents.append("გიორგი თედოზაშვილი")
                AllStudents.append("ნიკა დობო")
                break

    Index = 0
    while len(Students) > 0:
        Random = random.choice(Students)
        print(f"ვირჩევთ {Random} ჯგუფი {Index + 1} სთვის")
        Groups[Index].append(Random)
        AllStudents.append(Random)
        Students.remove(Random)
        Index += 1
        if Index == NumberOfGroups:
            Index = 0

    return Groups, AllStudents



































goa_group57_students = [i for i in range(100)]

Grouped, all = GetGroups(goa_group57_students)

def Tests():
    print("Testing")

    print("Test 1 Passed")

    for i in goa_group57_students:
        if i not in all:
            print(i)
            print("Test 2 Failed")
            return
        
    print("Test 2 Passed")

Tests()

def ChooseLeader(Group):
    LeaderIndex = random.randint(0, len(Group) - 1)
 
