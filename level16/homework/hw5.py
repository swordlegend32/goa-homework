# 5) დედამ გაგიშვათ აფთიაქში თავის ტკივილის წამლის საყიდლათ,
# ეს წამალი დღეში უნდა დალიო შენი წონის მიხედვით. 
# თუ 10 დან 20 კილომდე ხარ ნახევარი ტაბლეტი უნდა დალიო დღეში,
# თუ 30-40 კილომდე ხარ 1 ტაბლეთი ორჯერ დღეში და თუ 45 კილოზე მეტი ხარ სამი 
# ტაბლეტი უნდა დალიო ორჯერ დღეში. თქვენი მისიაა ამ ინფორმაციით გაარკვიოთ მომხარებელს 
# რამდენი წამალი აქვს დასალევი და დღეში რამდენჯერ უნდა დალიოს.

weight = int(input("your weight (kg): "))

if 10 <= weight <= 20:
    print("შენ უნდა დალიო ნახევარი ტაბლეტი დღეში 1-ჯერ.")
elif 30 <= weight <= 40:
    print("შენ უნდა დალიო 1 ტაბლეტი ორჯერ დღეში.")
elif weight > 45:
    print("შენ უნდა დალიო 3 ტაბლეტი ორჯერ დღეში.")
else:
    print("შენ ძალიან პატარა ხარ რომ წამლები სვა. ჯერ გაიზარდე")