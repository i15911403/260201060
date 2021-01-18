def SelectionSort(list):
  if len(list)==1:
    return [list[0]]
  else:
    for i in list:
      if i == min(list):
        list.remove(i)
        list.insert(0,i)
        return [list[0]]+SelectionSort(list[1:])

def BinarySearch(list,low,high,item):
  if high < low :
    return -1
  else:
    mid = (high + low) // 2
    if list[mid] == item:
      return mid
    elif list[mid] > item:
      return BinarySearch(list,low,mid-1,item)
    else:
      return BinarySearch(list,mid+1,high,item)

my_list = [22, 8, 12, -4, 27, 30, 36, 50, 7, 68, 91, 56, 2, 85, 42,98, 25]
my_list=SelectionSort(my_list)
print(BinarySearch(my_list,0,len(my_list)-1,50))