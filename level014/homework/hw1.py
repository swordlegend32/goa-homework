
# 1) თუ ასაკი არის 18 ის ზემოთ ან 50 წლის ქვემოთ  
# ან თუ  ასაკი  ნაკლებია 18 ზე და მეტია 50 ზე გამოტანეთ ის უნდა იყოს ან მოხუცი ან ახალგაზრდა

is_running = True

while is_running:
    try:
        Input = int(input("Enter Your Age: "))
        if Input > 18 and Input < 50:
            print("Proper Age Requierment Met")
            is_running = False
        elif Input <= 18:
            print("You Are Too Young")
        else:
            print("You are Too Old")
    except ValueError:
        print("Please Enter a Integer")

print(f"Welcome You Are: {Input} years old")