def ArrayAdditionI(lst):
    maxNum = max(lst)
    lst.remove(maxNum)
    count = 0
    listSum = sum(lst)
    diff = abs(maxNum - listSum)
    if listSum > maxNum:
        print True
    else:
        print False
    
    
        


ArrayAdditionI([5,7,16,1,2])        