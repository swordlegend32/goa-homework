#      7) მომხმარებელს შეეკითხეთ რიცხვი შემდეგ შექმენით ფუნქცია რომელსაც ექნება პარამეტრი რომელსაც არგუმენტად გადაეცემა მომხლარებლის შემოტანილი რიცხვი შემდეგ კი დაბეჭდავს ეს რიცხვი დადებითია თუ უარყოფითი

def check_number(num):
    return "Positive" if num > 0 else "Negative"

num = input("Enter a number: ")
print(check_number(int(num)))