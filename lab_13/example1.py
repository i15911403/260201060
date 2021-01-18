def SelectionSort(list):
  if len(list)==1:
    return [list[0]]
  else:
    for i in list:
      if i == min(list):
        list.remove(i)
        list.insert(0,i)
        return [list[0]]+SelectionSort(list[1:])
print(SelectionSort([3,1,4,2,7,5,9,10]))