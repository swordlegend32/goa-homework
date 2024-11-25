# 4)
# გამოიყენეთ or  რათა გაიგოთ  თუ ცხოველი არის , კატა თუ თაგვი.

Animals = ("Cat","Mouse","კატა","თაგვი")
Input = input("Enter (Cat or Mouse) ")


while Input.capitalize() not in Animals:
    Input = input("Please Enter (Cat or Mouse) ")

print(f"Your Animal Is {Input}")