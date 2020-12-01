my_dictionary = {}
count = 0
my_list = []
while count != 5 :
  name = input("Enter your name: ")
  salary = int(input("Enter your salary: "))
  my_dictionary[name] =salary 
  count+=1
print(my_dictionary)
for i,j in zip(my_dictionary.keys(),my_dictionary.values()):
  if j == max(my_dictionary.values()):
    print(i)
    my_dictionary.pop(i)
    break
  else : continue
for j,k in zip(my_dictionary.keys(),my_dictionary.values()):
  if k == max(my_dictionary.values()):
    print(j)
    my_dictionary.pop(j)
    break
  else : continue
for k,z in zip(my_dictionary.keys(),my_dictionary.values()):
  if z == max(my_dictionary.values()):
    print(k)
  else : continue








