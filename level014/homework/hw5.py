# 5)
# შეამოწმეთ, თუ ერთ-ერთი ციფრი უფრო დიდია 10-ზე ან მეორე ციფრი ნაკლებია 50-ზე

is_running = True

while is_running:
    try:
        Input1 = int(input("Enter Your Number (n > 10;): "))
        Input2 = int(input("Enter Your Number (n < 50;): "))
        if Input1 > 10 or Input2 < 50:
            print(f"{Input1} or {Input2} Meets The Proper Requierments")
            is_running = False
        elif Input1 <= 10 or Input2 >= 50 :
             print(f"{Input1} Is Too Small or {Input2} is too big")
        else:
            print("error")
    except ValueError:
        print("Please Enter a Integer")


print(f"Code Comleted 'Input1 Selected: {Input1}' 'Input2 Selected: {Input2}'")