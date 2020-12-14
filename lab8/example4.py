def binary_to_dec(a):
  sum = ""
  while a!=0:
    b = a%2
    a =  (a//2 )
    b = str(b)
    sum = b + sum
  return sum 

def dec_to_binary(a):
  a = str(a)
  count = 0
  sum = 0
  b = len(a)-1
  while count != len(a):
    sum += int(a[count])*2**b
    b -=1
    count+=1
  return sum

def main():
  print(binary_to_dec(18))
  print(dec_to_binary(10010))
main()




 

    











