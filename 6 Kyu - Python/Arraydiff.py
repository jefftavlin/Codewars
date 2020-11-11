def array_diff(a, b):
     for item in a:
         if item in b:
             a.remove(item)
     for item in a:
         try:
             if item in b:
                 a.remove(item)
         except ValueError:
             continue
     return a
     
