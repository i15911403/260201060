password = "1234"
while True :
  usernamepassword = input("Enter your password:(If you need help,write help.) ")
  if password == usernamepassword :
    print("Welcome")
    break
  elif usernamepassword == "help":
    print(password[0])
  else :
    print("Try again")