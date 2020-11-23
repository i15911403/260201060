n = int(input("Enter a number: ")) 
for i in range(n):
  print("") 
  for j in range(n):
    if i == j :
      print("1",sep=" ",end = " ")
    else :
      print("0",sep=" ",end =" " )