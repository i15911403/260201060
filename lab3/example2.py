x = float(input("Enter your number 1 : "))
y = float(input("Enter your number 2 : "))
z = float(input("Enter your number 3 : "))

if x<=y and y<=z:
  print(x)
elif y<=x and x<=z:
  print(x)
else:
  print(z)