# ორი რიცხვის გამოკლება
#  დაწერე პროგრამა, რომელიც შემოატანინებს მომხმარებელს ორი რიცხვს და დაბეჭდავს მათ სხვაობას.

num1 = input("პირველი რიცხვი: ")
num2 = input("მეორე რიცხვი: ")

while num1.isdigit() == False:
    num1 = input("პირველი რიცხვი: ")

while num2.isdigit() == False:
    num2 = input("მეორე რიცხვი: ")

print(float(num1) - float(num2))
