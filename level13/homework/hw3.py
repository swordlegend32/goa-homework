# 3) მომხმარებელს შემოატაინეთ თავისი სახელი, გვარი, ასაკი, და შემდეგ შეაერთეთ ისე რომ გამოვიდეს წინადადება.

name = input("სახელი: ")
surname = input("გვარი: ")
age = input("ასაკი: ")

while age.isdigit() == False:
    age = int(input("ასაკი: "))

print("თქვენი სახელია : " + name  + "; თქვენი გვარია : " + surname + "; თქვენ ხართ : " + age + "; წლის")