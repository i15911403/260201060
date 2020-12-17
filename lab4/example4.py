a = int(input("a :"))
b = int(input("b :"))
if b < 0 :
  print("Error")
elif a == 0 and b == 0:
  print("Error")
else :
  x = 1
  for i in range(1,b+1) :
    x *= a
  print("a**b =",x)