#  7) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს შემდეგ კი დაბეჭდავს ეს რიცხვი ლუწია თუ კენტი

def even_or_odd():
    x = int(input("Enter a number: "))
    if x % 2 == 0:
        print("luwi")
    else:
        print("kenti")

even_or_odd()