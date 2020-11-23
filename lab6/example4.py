elements = int(input("How many elements ? "))
c = 0
user_list = []
while c < elements :
  x = int(input("Enter your number: "))
  user_list.append(x)
  c += 1
user_list.sort()
user_list.reverse()
for i in user_list:
  if user_list.count(i) > 1 :
    user_list.remove(i)
  else :
    continue
print(user_list)