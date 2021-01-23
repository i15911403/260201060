def SelectionSort(list):
  if len(list) == 1:
    return [list[0]]
  else:
    for i in list:
      if i == min(list):
        list.remove(i)
        list.insert(0,i)
        return [list[0]]+SelectionSort(list[1:])

my_list = [13, 1, 27, 33, 14, 26, 72, 48, 16, 15, 6, 64, 79, 3, 39, 73, 93, 68, 41, 87, 28, 97,
67, 20, 29, 9, 12, 94, 94, 96, 88, 69, 49, 78, 91, 2, 47, 87, 29, 79, 18, 55, 88, 67,
37, 26, 51, 84, 85, 7, 84, 96, 91, 16, 28, 45, 98, 11, 92, 43, 59, 31, 58, 39, 76, 45,
26, 57, 52, 40, 82, 54, 94, 96, 4, 76, 6, 2, 44, 79, 56, 19, 71, 62, 10, 79, 86, 98,
5, 13, 5, 37, 17, 74, 75, 43, 46, 51, 94, 38, 30, 13, 5, 94, 4, 22, 6, 44, 40, 53, 69,
88, 41, 2, 54, 50, 21, 68, 81, 69]
print(my_list)
def MergeSort(nums):
  n = len(nums)
  if n > 1 :
    m = n // 2
    nums1,nums2 = nums[:m],nums[m:]
    MergeSort(nums1)
    MergeSort(nums2)
    merge(nums1,nums2,nums)


def merge(a,b,c):
  i1, i2, i3 = 0, 0, 0
  n1, n2 = len(a), len(b)
  while i1 < n1 and i2 < n2:
    if a[i1] < b[i2]:
      c[i3] = a[i1]
      i1 = i1 + 1
    else:
      c[i3] = b[i2]
      i2 = i2 + 1
    i3 = i3 + 1

  while i1 < n1:
    c[i3] = a[i1]
    i1 = i1 + 1
    i3 = i3 + 1
  while i2 < n2:
    c[i3] = b[i2]
    i2 = i2 + 1
    i3 = i3 + 1
MergeSort(my_list)
print(my_list)

