#5)

#num1 = 6
#num2 = 8
#num3 = 10
#average = num1 + num2 + num3 / 3
#print("Average:", average)

#შეასწორეთ კოდი ისე რომ საშუალო არითმეტიკული სწორად გამოითვალოს

# მათემატიკის პრიორიტეტის ცხრილი

# (). ფრჩხილები ოპერაცია ფრჩხილებში სრულდება პირველი
# ^/** ხარისხი. ხარისხის ოპერაციები სრულდება ფრჩხილების მერე
# *, / , %. გამრავლება გაყოფა და მოდულო სრულდება ხარისხის შემდეგ
# +,-. ბოლოს სრულდება გამოკლება და მიმატება

# ეს კოდი რომ გავასწოროთ უნდა ჩავსვაღ მიმატება რჩხილებში

num1 = 6
num2 = 8
num3 = 10
average = (num1 + num2 + num3) / 3
print("Average:", average)

# ესე დაწერილი მაინც უკეთესი იქნება

nums = [6,8,10]


def getAverage(numbers):
    avg = 0

    for x in range(len(numbers)):
         avg += numbers[x]
    avg /= len(nums)
    return avg


print("Average:", getAverage(nums))
