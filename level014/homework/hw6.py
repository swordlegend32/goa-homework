
# 6)
# შეამოწმეთ შეყვანილი სიტყვა hello-ა თუ hello world.

Words = ("hello","hello world")
Input = input("Enter (hello or hello world) ")


while Input.lower() not in Words:
   Input = input("Please Enter (hello or hello world) ")

print(f"Your Word Is {Input}")