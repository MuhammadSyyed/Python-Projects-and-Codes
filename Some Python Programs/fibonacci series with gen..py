def fab(a,b):
   true=1
   while true:
      x=int(input('enter number'))
      c = 0
      yield a
      yield b
      while c < x:
         d = a + b
         yield d
         a,b,d=b,d,a+b
         c += 1
