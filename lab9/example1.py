def harmonicsum(n):
  if n == 1 :
    return n
  else :
   return ( 1 / n ) + harmonicsum(n-1)
print(harmonicsum(5))