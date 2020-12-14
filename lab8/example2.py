def is_prime(n):
  if n<2 : 
    return False
  for i in range(2,n):
    if n%i == 0:
      return False
  return True

def print_primes_between(a,b):
  for i in range(a,b):
    if is_prime(i):
      print(i,end=" ")

def main():
  x = int(input("Begin: "))
  y = int(input("End: "))
  print_primes_between(x,y)

main()