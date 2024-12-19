
num = int(input("Enter Your Number: "))

for i in range(0,num,2):
    if i == 0:
        num = 0
    num += i

print(num)