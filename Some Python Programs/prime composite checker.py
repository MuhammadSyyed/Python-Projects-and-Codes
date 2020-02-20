x=int(input ('any number'))
for i in range(2,x):
    if x%i==0:
        print('composite Number')
        break
else:
    print('Prime Number')
