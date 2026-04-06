def rectangle(rows,cols):
   for i in range(rows):
      for j in range(cols):
         print("*", end="")
      print()
rows = 4
cols = 6
rectangle(rows,cols)