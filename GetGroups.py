import random
import time
import math
import sys


StudentsToGroup = [i for i in range(50)]

def GetGroups(Students,SPG):
    Groups = []
    AllStudents = []
    NumberOfGroups = 0
    MinGroups = 1
    StudentsPerGroup = SPG

    NumberOfGroups =  math.ceil(len(Students) / StudentsPerGroup)

    def BalanceNumInGroups():
        print("მოსწავლეების რაოდენობა არ არის ჯგუფების რაოდენობის გამრავლითი")
        answ = input("გსურთ გახანგრძლივოთ ჯგუფების რაოდენობა ან შეცვალოთ ჯგუფში ადამიანის რაოდენობა? (y/n/c): ")
        if answ == "y":
            return None,None
        elif answ == "n":
            sys.exit()
            pass
        elif answ == "c":
            StudentsPerGroup = int(input("შეიყვანეთ ჯგუფში მოსწავლეების რაოდენობა: "))
            NumberOfGroups = math.ceil(len(Students) / StudentsPerGroup)
            if len(Students) % StudentsPerGroup != 0:
                StudentsPerGroup,NumberOfGroups = BalanceNumInGroups()
            return StudentsPerGroup, NumberOfGroups

    if len(Students) % StudentsPerGroup != 0:
        NewStudentsPerGroup,NewNumberOfGroups = BalanceNumInGroups()
        if NewNumberOfGroups and NewStudentsPerGroup != None:
            StudentsPerGroup = NewStudentsPerGroup
            NumberOfGroups = NewNumberOfGroups
       
    
    print(f"ჯგუფების რაოდენობა: {NumberOfGroups}")
    print(f"მოსწავლე ყოველ ჯგუფში: {StudentsPerGroup}")

    Counting = (5,4,3,2,1)
    
    for i in Counting:
        print(f"Starting in {i}")
        time.sleep(1)

    for i in range(NumberOfGroups):
        Groups.append([])

    Priority_Students = ["გიორგი თედოზაშვილი", "ნიკა დობო"]
    group = random.choice(Groups)
    for i in range(NumberOfGroups):
        group = random.choice(Groups)
    for i in Priority_Students:
        if len(group) < StudentsPerGroup:
            group.append(i)
            # Students.pop(Students.index(i))
            AllStudents.append(i)

    Index = 0
    while len(Students) > 0:
        
        if Index == NumberOfGroups:
                Index = 0

        Random = random.choice(Students)
        if Random in AllStudents:
            Students.remove(Random)
            continue
        Groups[Index].append(Random)
        AllStudents.append(Random)
        Students.remove(Random)

        Index += 1

        if Index == NumberOfGroups:
                Index = 0

        if len(Groups[Index]) >= StudentsPerGroup:
            Index += 1
            if Index == NumberOfGroups:
                Index = 0
            continue  

    return Groups, AllStudents


def ChooseLeader(Group):
    LeaderIndex = random.randint(0, len(Group) - 1)
    return Group[LeaderIndex]

















































def Tests(goa_group57_students, Grouped, all):
    print("Testing")

    print("Test 1 Passed")

    for i in goa_group57_students:
        if i not in all:
            print(i)
            print("Test 2 Failed")
            return
        
    print("Test 2 Passed")
































































goa_group57_students = ["თორნიკე ბერიძე",
"დიანა ძუკაევი",
"ლუკა კელეპტრიშვილი",
"jorj kacitadze",
"გვანცა კოპაძე" ,
"გიორგი გუგავა",
"ლაშა კაჭიური",
"ნიკა გიგოშვილი",
"ლუკა გიგოშვილი"
"თორნიკე ზუბიაშვილი",
"საბა რუსიეშვილი"
"გიორგი ჩადუნელი"
"ნიკა დობო"
"ქეთევან მახარაშვილი",
"გიორგი თედოზაშვილი"
"ლუკა მიქუტიშვილი",]

Grouped, all = GetGroups(goa_group57_students,3)



Tests(goa_group57_students, Grouped, all)

print(Grouped)
for i in Grouped:
    print(f"Group {Grouped.index(i) + 1}: {i}")