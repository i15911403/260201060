email_address = "ceng113@example.com"
user_email_address = input("email address: ")
if user_email_address == email_address :
  print("Your email address is",user_email_address)
elif email_address.upper()== user_email_address :
  print("Your email address is",email_address.lower())
else :
  print("Try again")