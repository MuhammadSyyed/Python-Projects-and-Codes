def prime(n):
    for i in range(2,n+1):
        y=0
        for j in range(2,i):
            if(i%j==0):
                y=y+1
        else:
            yield i
            
            
