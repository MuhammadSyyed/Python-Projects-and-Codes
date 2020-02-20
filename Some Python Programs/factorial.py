true=1
while true:
    x=int(input('Enter any number:'))
    if x<0:
        print('ERROR:Enter positive interger')
    elif x==0:
        print('1')
    else:
        for i in range(1,x):
            x=i*x
        print(x)
        
