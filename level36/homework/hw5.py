#      5) მომხმარებელს შეეკითხეთ ორი რიცხვი შემდეგ შექმენით ფუნქცია რომელსაც ექნება ორი პარატემტრი რომელსაც არგუმენტად გადაეცემა მომხლარებლის შემოტანილი რიცხვები შემდეგ კი დაბეჭდავს მათ განაყოფს

def divide(x,y):
    return x // y

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print(divide(x,y))