import random
num = [i for i in range(1,31)]

while True:
    user_num = int(input("Enter  Your Number: "))
    ChosenNumber = random.randint(1, 30)
    if user_num == ChosenNumber:
        print("You guessed the number!")
        break
    elif user_num <= 30 and user_num >= 1 and user_num != ChosenNumber:
        print("Incorrect, Please try again")
    else:
        print("You must enter a number from 1 to 30")
        continue
