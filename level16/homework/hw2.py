# 2) მომხმარებელს შემოატანინეთ ასაკი, 
# გაარკვიეთ მას შეუძლია თუ არა მართვის მოწმობის აღება 
# (17 წლის უნდა იყო მართვის მოწმობის აღება რომ შეგეძლოს). 
# თუ შეუძლია უთხარით რომ ის დიდი ბიჭი ან გოგოა, თუ არა დაუპრინტეთ რომ მალე გაიზრდება.

age = None

running = True

while running:
    try:
        age = int(input("Enter Your Age: " ))
        running = False
        break
    except ValueError:
        print(f"{age} is not a valid integer. please enter a valid integer")

if age >= 17:
    print(f"შენ შეგიძლია აიღო მართვის მოწმობა {age} წლის ასაკში. შენ დიდი ბიჭი/გოგო ხარ")
else:
    print(f"შენ არ შეგიძლია აიღო მართვის მოწმობა {age} წლის ასაკში. შენ მალე გაიზრდები")

