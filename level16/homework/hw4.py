# 4) გიორგიმ შექმნა ზოოპარკი სადაც შესვლა მხოლოდ კონკრეტული
# აღნაგობის ხალხს შეუძლიათ. გიორგი ზოოპარკში უშვებს ხალხს რომელიც
# 180 სანტიმეტრზე მაღლები არიან და 50-90 კილოს შორის არიან წონით.
# თქვენი მისიაა რომ მომხმარებელს შემოატანინოთ წონა და სიმაღლე და 
# გაარკვიოთ შეუძლია თუ არა მომხმარებელს ზოოპარკის მონახულება.

height = int(input("your height (cm): "))
weight = int(input("your weight (kg): "))

if height >= 180 and 50 <= weight <= 90:
    print("თქვენ შეგიძლიათ მოინახულოთ ზოოპარკი!")
else:
    print("სამწუხაროდ, თქვენ ვერ შეძლებთ ზოოპარკში შესვლას.")