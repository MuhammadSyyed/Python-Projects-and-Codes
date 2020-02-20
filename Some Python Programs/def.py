def common (l1,l2):
    for i in l1:
        if i in l2:
            print(i,'is common')
        if i not in l2:
            print(i, 'is not common')
