tets_variable=[]
second_variable=[]
def power(var):
    for i in str(var):
        if (i !=  '^'):
            tets_variable.append(i)
        elif (i == '^'):
            q=0
        else:
            second_variable.append(i)
    answer=int(tets_variable) ** int(second_variable)
    return answer
power(3^3)
