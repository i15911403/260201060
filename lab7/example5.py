password = input("Enter your password: ")
normal_password,lower_password,upper_password = [],[],[]
for i in password.lower():
  lower_password.append(i)
for i in password.upper():
  upper_password.append(i)
lower_password,upper_password= set(lower_password),set(upper_password)
for i in password :
  normal_password.append(i)
normal_password=set(normal_password)
if len(password) >= 8:
  if len(normal_password.difference(lower_password)) >= 1 :
    if len(normal_password.difference(upper_password)) >= 1 :
      if len(upper_password.intersection(lower_password)) >= 1 :
        print("valid password")
      else:
        print("invalid password")
    else:
      print("invalid password")
  else:
    print("invalid password")
else :
  print("invalid password")
