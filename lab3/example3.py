GPA = float(input("Enter your GPA : "))
lectures = int(input("Enter your lectures : "))

if GPA < 2 and  lectures < 47:
   print("Not enough number of lectures and GPA!")
elif GPA >=2 and lectures < 47:
   print("Not enough GPA!")
elif GPA >=2 and lectures < 47:
    print("Not enough number of lectures.")
else  :
     print("GRADUATED")