# 8) მომხმარებელს შეეკითხეთ რიცხვი შემდეგ შექმენით ფუნქცია რომელსაც ექნება პარამეტრი რომელსაც არგუმენტად გადაეცემა მომხლარებლის შემოტანილი რიცხვი შემდეგ კი თუ 18 ზე უთხრას რომ სრულწლოვანია თუარადა არარის

def is_adult(age):
    if age >= 18:
        return True
    else:
        return False
    
age = int(input("Enter your age: "))

if is_adult(age):
    print("You are an adult")
else:
    print("You are not an adult")

