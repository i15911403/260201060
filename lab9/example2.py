def reverse(my_list):
  if len(my_list) == 0 :
    return []
  else:
    return [my_list.pop()] + reverse(my_list)
    
print(reverse([1,2,3,4,5]))