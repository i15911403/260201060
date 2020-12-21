def evennumber(my_list):
  if len(my_list) == 0 :
    return 0
  count = 0
  if my_list[0] % 2 == 0 :
    count += 1
  return count + evennumber(my_list[1:])

print(evennumber([0,1,2,3,4,5]))