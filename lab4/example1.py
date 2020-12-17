x = int(input("Enter your number :"))
x = str(x)
if len(x) == 1 :
  a = x[len(x)-1]
  print(int(a)+0)
else :
  y = x[len(x)-1]
  z = x[len(x)-2]
  print(int(y)+int(z))