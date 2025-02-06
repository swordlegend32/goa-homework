# 8) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიღხვს შემდეგ კი დაბეჭდავს დადებითია თუ უარყოფითი

def nums():
    x = int(input("Enter a number: "))
    if x > 0:
        print("dadebiti")
    elif x == 0:
        print("nuli")            
    else:
        print("uaryofiti")

nums()        