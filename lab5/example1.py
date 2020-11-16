number = int(input("Enter your number: "))
for i in range(1,11):
  if number < 0 or number >= 10 :
    print("Please enter valid number.")
    break
  else:  
    print(number,"x",i,"=",number*i)