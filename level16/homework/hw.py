# 1) მომხმარებელს შემოატანინეთ თავიანთი სახელი, 
# თუ ეს სახელი ემთხვევა თქვენს სახელს დაუპრინტეთ რომ ერთნაირი სახელები გაქვთ,
# სხვა შემთხვევაში დაუპრინტეთ რომ სასიამოვნოა მათი გაცნობა.

name = input("enter your name: ")

if name.upper() == "GIORGI" or name == "გიორგი" or name.upper() == "GIO" or name == "gio":
    print(f"ჩემი სახელიც არის {name}.")
else:
    print(f"სასიამოვნოა შენი გაცნობა {name}.")