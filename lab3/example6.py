a = float(input("a :"))
b = float(input("b :"))
c = float(input("c :"))

delta = b**2 -4 * a * c
x1 = (-b + delta**0.5) / 2*a
x2 = (-b - delta**0.5) / 2*a
if delta > 0 :
  print("There are two real roots.x1 = {} and x2 = {}".format(x1,x2))
elif delta == 0:
  print("There is one real root.x1 = {}".format(x1))
else :
  print("There are two complex roots.")