numbers = int(input("How many number? "))
a = 1
b = 1
fibonacci = [a,b]
for i in range(numbers-2):
  a,b = b,a+b
  fibonacci.append(b)
print(fibonacci)