grades = []
n = int(input("How many student? "))
for i in range(n):

  midterm1 = float(input("midterm 1: "))
  midterm2 = float(input("midterm 2: "))
  final_exam = float(input("final exam: "))
  grades.append([midterm1,midterm2,final_exam])

print(grades)