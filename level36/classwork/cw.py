
class Calculator():

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def Sum(self):
        return self.x + self.y

    def Mult(self):
        return self.x * self.y

    def Div(self):
        return self.x / self.y

    def FloorDiv(self):
        return self.x // self.y

    def Pow(self):
        return self.x ** self.y
    
    def RSum(self):
        return self.y + self.x

    def RMult(self):
        return self.y * self.x

    def RDiv(self):
        return self.y / self.x

    def RFloorDiv(self):
        return self.y // self.x
    def RPow(self):
        return  self.y ** self.x
    
    
Calc = Calculator(5,3)

print(Calc.Sum())
print(Calc.Mult())
print(Calc.Div())
print(Calc.FloorDiv())
print(Calc.Pow())
print(Calc.RSum())
print(Calc.RMult())
print(Calc.RDiv())
print(Calc.RFloorDiv())
print(Calc.RPow())


