books=["ULYSESS","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
book_dictionary = {}
for i in books:
  a = len(i)
  b = len(list(set(i)))
  book_dictionary[i]=(a,b)
print(book_dictionary)
