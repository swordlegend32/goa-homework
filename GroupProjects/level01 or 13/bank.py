
Precentege = 2

def Deposit(amount,BankBalance,On_Hand):
    if float(amount) > On_Hand:
        print("----------------------------------------------------------------")
        print("Not Enough Money To Deposit ❌")
        return BankBalance,0
    Money = BankBalance + float(amount)
    return Money,float(amount)

def Withdraw(amount,BankBalance):
    if BankBalance - float(amount) < 0:
        print("----------------------------------------------------------------")
        print("Insufficent Balance ❌")
        return BankBalance
    else:
        Money = BankBalance - float(amount)
        return Money

def Start(Balance):

    BankBalance = Balance
    On_Hand = 500
    Pay = 1250
    Count = 0
    Dept = 0

    while True:
        tp = input("Withdraw [1] ⬆, Deposit [2] ⬇, Loan [3] 🏦, Balance [4] 💼, Exit [5] 🚫; ")
        if tp == "Withdraw" or tp == "1":
            amount = input("Amount: ")
            BankBalance = Withdraw(amount,BankBalance)
            Count += 1
            print("----------------------------------------------------------------")
            print("Your Balance Is: " + str(BankBalance) + "$ 💳")
            print("----------------------------------------------------------------")
        elif tp == "Deposit" or tp == "2":
            amount = input("Amount: ")
            BankBalance,Deduction = Deposit(amount,BankBalance,On_Hand)
            On_Hand -= Deduction
            Count += 1
            print("----------------------------------------------------------------")
            print("Your Balance Is: " + str(BankBalance) + "$ 💳")
            print("Your Cash Is: " + str(On_Hand) + "$ 💵")
            print("----------------------------------------------------------------")
        elif tp == "Balance" or tp == "4":
            print("----------------------------------------------------------------")
            print("Your Balance Is: " + str(BankBalance) + "$ 💳")
            print("Your Cash Is: " + str(On_Hand) + "$ 💵")
            print("Your Owe: " + str(Dept) + "$ 📉")
            print("----------------------------------------------------------------")
            print("Your Pay Is: " + str(Pay) + "$ 📈 Every 3 Turns")
            print("Your Interest Is: " + str(Precentege) + "$ 📈 Every 3 Turns")
            print("----------------------------------------------------------------")
        elif tp == "Loan" or tp == "3":
            Loan = input("Loan [1], Pay [2]; ")
            if Loan == "Loan" or Loan == "1":
                amount = float(input("Loan Amount: "))
                On_Hand += float(amount)
                Dept = amount + (amount  * Precentege) / 100
            elif Loan == "Pay" or Loan == "2":
                 Type = input("Cash [1], Balance [2]; ")
                 if Type == "Cash" or Loan == "1":
                    amount = float(input("Pay : "))
                    if On_Hand - amount <= 0:
                        print("----------------------------------------------------------------")
                        print("Not Enough Cash! ❌")
                        print("Your Cash Is: " + str(On_Hand) + "$ 💵")
                        print("----------------------------------------------------------------")
                    else:
                        if Dept - amount < 0:
                            amount = Dept
                        Dept -= amount
                        On_Hand -= amount
                        print("----------------------------------------------------------------")
                        print("You Now Owe: " + str(Dept) + "$ 📉")
                        print("----------------------------------------------------------------")
                 elif Type == "Balance" or Loan == "2":
                    amount = float(input("Pay : "))
                    if BankBalance - amount <= 0:
                        print("----------------------------------------------------------------")
                        print("Not Enough Balance! ❌")
                        print("Your Balance Is: " + str(BankBalance) + "$ 💳")
                        print("----------------------------------------------------------------")
                    else:
                        if Dept - amount < 0:
                            amount = Dept
                        Dept -= amount
                        BankBalance -= amount
                        print("You Now Owe: " + str(Dept) + "$ 📉")
                 
        elif tp == "Exit" or tp == "5":
            print("----------------------------------------------------------------")
            print("Your Final Balance Is: " + str(BankBalance) + "$ 💳")
            print("Your Final Cash Is: " + str(On_Hand) + "$ 💵")
            print("Your Final Dept Is: " + str(Dept) + "$ 📉")
            print("----------------------------------------------------------------")
            break
        else:
            print("----------------------------------------------------------------")
            print("Invalid Input; Please Enter Valid Input ❌;")
            print("----------------------------------------------------------------")
        if Count == 3:
            if Dept:
                Amount = BankBalance + (BankBalance  * 10) / 100
                if Dept - Amount < 0:
                    Amount = Dept
                Dept -= Amount
                Balance -= Amount

            BankBalance = BankBalance + (BankBalance  * Precentege) / 100
            On_Hand += Pay
            Count = 0
            print("----------------------------------------------------------------")
            print("Your Balance Increased By " + str(Precentege) + "% Your Balance Is : " + str(BankBalance) + "$ 💳")
            print("Your Cash Increased By " + str(Pay) + " Your Cash Is : " + str(On_Hand) + "$ 💵")
            print("----------------------------------------------------------------")
            print("You Owe: " + str(Dept) + "$ 📉")
            print("----------------------------------------------------------------")

Start(0)
