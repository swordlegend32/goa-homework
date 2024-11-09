#1)
#a = 5
#b = "10"
#result = a + b
#print("Result:", result)

# კოდი გამოიტანს ერორს დაწერეთ რატომ და ასევე ცალკე დაწერეთ სწორი ფორმა 

# expected error cant do math with string and number არ შეიძლება არითმეტიკული ოპერაცია გაკეთდეს სტრინგსა და რიცხს შორის

# fix:

a = 5
b =  int("10")
result = a + b
print("Result: ", result)
