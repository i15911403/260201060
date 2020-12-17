n = int(input("Enter your number :"))
y = 1
for i in range(1,n+1):
  y *= i
print(n,"!=",y,sep="")