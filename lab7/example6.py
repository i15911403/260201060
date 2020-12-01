numbers1 = [2,3,4,20,5,5,15]
numbers2 = [10,20,20,15,30,40]
numbers1 = set(numbers1)
numbers2 = set(numbers2)
union_list = []
intersection_list = []
for i in numbers1:
  union_list.append(i)
for i in numbers2:
  if i in union_list:
    intersection_list.append(i)
  else:
    union_list.append(i)
print(intersection_list)
print(union_list)

