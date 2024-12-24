import os
import time
import json
import base64

# os = operating system time = time json = json წაკითხვისთვის/დაწერისთვის base64 = base64 ენქოდისთვის 

file_path = os.path.expanduser("~/Desktop/username_and_password.json") # ფაილის ადგილი კომპოუტერში

def encode(data): # ენქოდირება ფუნქცია
    return base64.b64encode(data.encode()).decode() # ენკოდირება base64 ით

def decode(data): # დეკოდირების ფუნქცია
    missing_padding = len(data) % 4 # პადდინგის დამატება თუ საჭიროა რადგან თუ არ არის სწორი პადდინგი ერრორს იზავს
    if missing_padding: # თუ არ არის სწორი პადდინგი
        data += '=' * (4 - missing_padding) # შეცვალე პადდინგი
    return base64.b64decode(data.encode()).decode() # დეკოდირება base64 ით

if os.path.exists(file_path): # თუ ფაილი არსებობს
    with open(file_path, 'r') as file: # წაიკითხე
        data = json.load(file) # აიღე ინფორმაცია ფაილიდან
        username = decode(data['username']) # დეკოდირება სახელის
        password = decode(data['password']) # დეკოდირება პაროლის
else: # თუ ფაილი არ არსებობს
    username = input("Enter a new username: ") # შეიყვანე ახალი სახელი
    password = input("Enter a new password: ") # შეიყვანა ახალი პაროლი
    data = {'username': encode(username), 'password': encode(password)} # ინფორმაცია რასაც შევინახავთ ფაილში 
    with open(file_path, 'w') as file: # გახსენი ფაილი და დაწერე (ახალი ინფორმაციის შეყვანა)
        json.dump(data, file) # ჩადე ინფორმაცია სახელის და პაროლის ფაილში
    os.chmod(file_path, 0o444) # გააკეთე ფაილი მარტო წაკითხვისთვის

Input_username = input("Enter Your Username: ") 
Input_password = input("Enter Your Password: ")

count = 0

# ამის ახსნა არ მჭირდება

while Input_username != username or Input_password != password:
    count += 1
    if count >= 3:
        print("You have exceeded the number of attempts. Please Wait 5 seconds")
        time.sleep(5) # დაიცადე 5 წამი
        count = 0
    else:
        print("Incorrect username or password please try again.")
        Input_username = input("Enter Your Username: ")
        Input_password = input("Enter Your Password: ")

print("Welcome To My Account Society.")