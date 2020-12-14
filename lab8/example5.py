def password_checker(password):
  level = 0
  if " " in password or len(password) < 8 :
    return level
  else:
    alpha,numeric,special = [],[],[]
    for i in password:
      if i.isalpha():
        alpha.append(i)  
      elif i.isnumeric():
        numeric.append(i)
      else:
        special.append(i)
  if len(alpha) > 0 :
    level += 1
  if len(numeric) > 0 :
    level +=1
  if len(special) > 0:
    level+=1
  return level
def main():
  password=input("Enter a password: ")
  print("Level:",password_checker(password))
main()