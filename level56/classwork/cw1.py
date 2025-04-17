
def Summed(n:int) -> int:
    ans = 0
    for i in range(1,n):
        ans += i
    return ans

print(Summed(5))
print(Summed(7))
print(Summed(12))
# ერრორს გამოიტანს იმიტომ რომ ტიპის ჩეკერს ვუთხარო რომ ინტეგერი უნდა მიიღოს და ინტეგერი უნდა დააბრუნოს
print(Summed('ada'))