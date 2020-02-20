def fab(a,b):
   true=1
   while true:
      x=int(input('enter number'))
      c = 0
      print(a)
      print(b)
      while c < x:
         d = a + b
         print(d)
         a,b,d=b,d,a+b
         c += 1
