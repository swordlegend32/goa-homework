# 3)
# შეამოწმეთ, არის თუ არა მოცემული ციფრი დადებითი ან ნული, თუმცა არ არის უარყოფითი.

is_running = True

while is_running:
    try:
        Input = int(input("Enter Your Positive Number "))
        if Input >= 0:
            print(f"{Input} Meets The Proper Requierments")
            is_running = False
        else:
            print(f"{Input} Is Not A Positive Integer")
    except ValueError:
        print("Please Enter a Integer")


print(f"Code Comleted 'Input Selected: {Input}'")