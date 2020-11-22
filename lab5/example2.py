numbers = int(input("How many numbers ? "))
numbers_list = []
even_numbers = []
odd_numbers = []
if numbers <= 0 :
  print("Please enter valid numbers")
else : 
  for i in range(1,numbers+1):
    x = int(input("Enter integer : "))
    numbers_list.append(x)
for j in numbers_list :
    if j % 2 == 0 :
      even_numbers.append(j)
    else :
      odd_numbers.append(j)
x = int(len(even_numbers))
y = int(len(numbers_list))
print("%",(x/y)*100)
