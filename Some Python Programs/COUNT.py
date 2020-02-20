x=int(input("Enter Any Number"))
for i in range(1,x+1):
    c=str(i)
    if len(c)>1 and c[-2]=='1':
        if c[-1]=='1' or c[-1]=='2' or c[-1]=='3':
            print(c,'th')
        else:
            print(c,'th')
    elif c[-1]=='1':
        print(c,'st')
    elif c[-1]=='2':
        print(c,'nd')
    elif c[-1]=='3':
        print(c,'rd')
    else:
        print(c,'th')
