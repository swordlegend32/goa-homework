#ციფრის გამრავლება 2-ზე
# დაწერე პროგრამა, 
# რომელიც მომხმარებელს შემოატანინებს რიცხვს, დაპრინტავს ჯერ ამ რიცხვს და შემდეგ ამ რიცხვის ნამრავლი 2-ზე.

# მოცემული რიცხვის გამრავლება 10-ზე
#  დაწერე პროგრამა, რომელიც მომხმარებელს შემოატანინებს რიცხვს, დაპრინტავს ჯერ ამ რიცხვს და შემდეგ ამ რიცხვის ნამრავლი 10-ზე.

number = input("რიცხვი: ")

while number.isdigit() == False:
    number = input("რიცხვი: ")

number = int(number)

print(number)
print(number * 2)