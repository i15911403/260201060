def hailstone(n):
  if n == 1 :
    return [] + [int(n)]
  else:
    if n % 2 == 0 :
     return []+ [int(n)] + hailstone(n / 2)
    else :
     return []+ [int(n)] + hailstone(3*n+1)
print(hailstone(11))