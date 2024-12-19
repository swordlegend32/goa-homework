
num = int(input("Enter Your Number: "))

for i in range(1,num,2):
    if i == 1:
        num = 0
    num += i

print(num)