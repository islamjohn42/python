# if/else

ism = input("Enter your name?\n>>>")
if ism.lower() != "ali":
  print(f"Sorry {ism.title()} we are waiting Ali")
else:
  print(f"Welcome back, {ism.title()}")

#################################
userAge = int(input("Enter your age: "))
if userAge >= 18:
  print("Welcome to the website")
else:
  print(f"Your age is {userAge}, Unfortunatly you are not allowed")

#################################

userLogin = str(input("Enter new login: \n>>>"))
if len(userLogin) <= 5:
  print("Your login should be more than 5 symbols")