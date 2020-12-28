def sum_list(n):
  if not isinstance(n,list):
    return n
  else:
    sum = 0
    for i in n :
      sum += sum_list(i)
    return sum  
print(sum_list([1,2,3,[10,20],14]))

    
       