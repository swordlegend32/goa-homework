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
    HighestStudentsPerGroup = 0

    for i in range(MinGroups, 9999):
        StudentsPerGroup = 3
        NumberOfGroups =  math.ceil(len(Students) / StudentsPerGroup)

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
        AllStudents.append(Random)
        Students.remove(Random)
        Index += 1
        if Index == NumberOfGroups:
            Index = 0

    return Groups,AllStudents




































goa_group57_students = ["თორნიკე ბერიძე", "ნიკა დობო", "გიორგი თედოზაშვილი", "ლაშაგიორგი", "ალექსანდრე კეკოშვილი",   "ნიკა გიგოშვილი", "ლუკა გიგოშვილი","ბექა ვარდუკაძე", "ბუბუნაური", "გვანცა კოპაძე", "გიორგი გუგავა", "გიორგი მოდებაძე", "ნიკა ტაბატაძე", "ქეთევან მახარაშვილი", "დიანა ძუკაევი", "ირაკლი ახალაია", "გიორგი კაციტაძე", "თორნიკე ზუბიაშვილი", "ლუკა კელეპტრიშვილი", "თორნიკე ხურცია", "ლაშა კაჭიური"]

print(len(goa_group57_students))

Grouped,all = GetGroups(goa_group57_students)

# for i in Grouped:
#     for x in i:
#         if x not in goa_group57_students:
#             print(x)
#             print("შეცდომა")
#             break

for i in goa_group57_students:
    if i not in all:
        print(i)
        print("შეცდომა")


def ChooseLeader(Group):
    LeaderIndex = random.randint(0, len(Group) - 1)
    if "გიორგი თედოზაშვილი" in Group:
        return "გიორგი თედოზაშვილი"
    return Group[LeaderIndex]

for i in range(len(Grouped)):
    print(f"ჯგუფი {i + 1}: {Grouped[i]}")
    print(f"ჯგუფის ლიდერი: {ChooseLeader(Grouped[i])}\n")