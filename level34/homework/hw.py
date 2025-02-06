
def CalculatorFunction(String):

    # order of operations
    # 1. Parentheses ill add later
    # 2. Exponents
    # 3. Multiplication and Division
    # 4. Addition and Subtraction
    Exponents =   []
    MultDiv =     []
    AddSub =      []

    for i in String:
        if i == '^':
            Exponents.append(i)
        elif i == '*' or i == '/':
            MultDiv.append(i)
        elif i == '+' or i == '-':
            AddSub.append(i)