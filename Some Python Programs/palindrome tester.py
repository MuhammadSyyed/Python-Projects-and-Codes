x=1
while x :
    x = input('Enter any word')
    if len(x)>1 and x==x[::-1]:
        print ('The word which you have provided is a palindrome')
    elif len(x)==1:
        print ('No, the given word is not a palindrome')
        continue
    else:
        print ('No, the given word is not a palindrome')
