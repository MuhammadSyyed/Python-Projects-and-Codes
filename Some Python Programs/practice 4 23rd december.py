def abc(x):
    if x>0 :
        print('x is positive')
        if x%2==0:
            print('x is even')
        else:
            print('x is odd')
    elif x<0 :
        print('x is negative')
        if x%2==0:
            print('x is even')
        else:
            print('x is odd')
    else:
        print('x is neutral')
        print('x is neither even not odd')
