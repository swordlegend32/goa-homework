# 12) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს შემდეგ კი ერთიდან იმ რიცხვამდე დაბეჭდავს ყველა კენტ რიცხვს

def nums():
    x = int(input("Enter a number: "))
    for i in range(1, x + 1, 2):
        print(i)

nums()