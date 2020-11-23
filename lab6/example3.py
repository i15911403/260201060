s = 0
grades = []
n = int(input("How many student? "))
for i in range(n):

  midterm1 = float(input("midterm 1: "))
  midterm2 = float(input("midterm 2: "))
  final_exam = float(input("final exam: "))
  total = midterm1 + midterm2 + final_exam
  if total / 3 > 90 :
     grades.append([midterm1,midterm2,final_exam])
     s += 1
  else:
    continue
print(s,"students",grades)
  

