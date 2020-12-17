number1 = int(input("Enter number1 : "))
number2 = int(input("Enter number2 : "))
x = 0
while True :
  a = number1 % 10
  b = number2 % 10
  number1 = number1 // 10
  number2 = number2 // 10
  if number1 == 0 or number2 == 0:
    if a == b :
      x += 1
      break
    else :
      break
  elif a == b :
    x += 1 
  else:
    continue
print(x)