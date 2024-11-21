# 2) 
# გამოიყენეთ or ოპერატორი, რათა შეამოწმოთ, თუ მოცემული ციფრები არიან 10-ზე მეტი ან 50-ზე ნაკლები.


is_running = True

while is_running:
    try:
        Input = int(input("Enter Your Number (n > 10;n < 50): "))
        if Input > 10 or Input < 50:
            print(f"{Input} Meets The Proper Requierments")
            is_running = False
        elif Input <= 10:
             print(f"{Input} Is Too Small")
        else:
            print(f"{Input} Is Too Large")
    except ValueError:
        print("Please Enter a Integer")


print(f"Code Comleted 'Input Selected: {Input}'")