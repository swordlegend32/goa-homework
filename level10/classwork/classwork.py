

name = input("თქვენი სახელი: ")

while len(name) < 3 or any(str.isdigit() for str in name):
    name = input("თქვენი სახელი: ")

print("გამარჯობა: ", name)
