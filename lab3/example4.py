age = int(input("What is your age ? "))
normal_bus_ticket_price = 3

if age < 6 or age > 60 :
  print("free")
elif age >= 6 and age < 18 :
  print(normal_bus_ticket_price*1 / 2,"TL")
else :
  print(normal_bus_ticket_price,"TL")