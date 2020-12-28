def multiply(n):
  if n == 1 :
    return 3
  else:
    return multiply(n-1) + 3

print(multiply(5))