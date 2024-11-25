#  7) 
#  ახსენით კომენტარებით ყველა დავალება

# is_running = True # ვქმნით ახალ ცვლადს რომლის ფუნქციაა რომ კოდი განაგრძოს სანამ ჩვენ არ მივაღწევთ პასუხს

# while is_running: # ვქმნით while ლუპს და ვიყენებთ is_running ცვლადს
#     try: # try კოდი რაც აქ არის მოთავსებული თუ შეხვდება ერრორი არ შევწყვიტავთ
#         Input = int(input("Enter Your Age: ")) # ვითხოვთ inputs რომელიც იქნება რიცხვი
#         if Input > 18 and Input < 50: # ვამოწმებთ თუ ჩვენი რიცხვი არის 18 ზე დიდი და 50 ზე დაბალი
#             print("Proper Age Requierment Met")
#             is_running = False # ვაჩრებთ ლუპს
#         elif Input <= 18: # თუ ჩვენი რიცხვი 18 ის როლია ან დაბალია 
#             print("You Are Too Young")
#         else: # თუ ის 50 ზე დიდია
#             print("You are Too Old")
#     except ValueError: # თუ ჩვენი Input არ არის რიცხვი
#         print("Please Enter a Integer")

# print(f"Welcome You Are: {Input} years old") 

# Animals = ["Cat","Mouse","კატა","თაგვი"] ვქმნით tuples სადაც ვინახავთ ჩვენ ცხოველებს სია რომელიც უნდა იყოს ინპუტში
# Input = input("Enter (Cat or Mouse) ")


# while Input.capitalize() not in Animals: # ვამოწმებთ თუ ჩვენი შემოტანილი input არის თუ არა ჩვენ tuple ში
#     Input = input("Please Enter (Cat or Mouse) ") # თუ არ არის თავიდან ვითხოვთ input'ს

# print(f"Your Animal Is {Input}")