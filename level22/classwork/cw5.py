
num = int(input("Enter Your Number: "))
Index = 0
sum = 0

while num > Index and num >= 5:
    Index += 5
    if Index >= num:
        break
    sum += Index

print(sum)
