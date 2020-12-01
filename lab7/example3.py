books=["ULYSESS","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
book_dictionary = {}
for i in books:
  a = len(i)
  b = len(set(i))
  c = (a + b) / 2
  book_dictionary[i]=(a,b,c)
print(book_dictionary)
  
  
  
  

  
  
  
