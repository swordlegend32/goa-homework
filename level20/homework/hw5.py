Text1 = "ლუწია"
Text2 = "კენტია"

for Index in range(0,101):
    print(f"{Index} {Text1 if Index % 2 == 0 else Text2}")