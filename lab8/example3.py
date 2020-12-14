def get_rand_list(b=0,e=10,N=5):
 import random
 a = random.sample(range(b,e),N)
 b = random.sample(range(b,e),N)
 print(a)
 print(b)
 print(get_overlap(a,b))

def get_overlap(list1,list2):
  list3 = []
  for i in list1:
    if i in list2:
      list3.append(i)
  return list3

get_rand_list()

