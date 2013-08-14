def  SimpleMode(lst) :
    mode =[]
    for i in lst:
        if lst.count(i) >1:
            mode.append(i)
    return mode[0]
    
print SimpleMode([10, 4, 5, 2, 4])