import time

def timer(n):
  if n == 0:
    print("STOP!")
    return 0
  print("Remaining time:",n)
  time.sleep(1)
  return timer(n-1)

timer(5)
  