x = float(input("ENter your number 1 : "))
y = float(input("ENter your number 2 : "))
z = float(input("ENter your number 3 : "))

if x<=y and y<=z:
  print(x)
elif y<=x and x<=z:
  print(x)
else:
  print(z)