#  10) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს შემდეგ კი ერთიდან იმ რიცხვამდე დაბეჭდავს ყველა რიცხვს

def nums():
    x = int(input("Enter a number: "))
    for i in range(x + 1):
        print(i)

nums()       