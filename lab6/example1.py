str = ""
email = input("Email: ")
email = email.lower()
for i in email :
  if i == "@":
    break
  else :
    if i == ".":
      continue
    else :
      str = str+i
email = str+"@example.com"
print(email)




