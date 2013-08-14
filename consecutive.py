def Consecutive(lst):
    newlst =[]
    minNum = min(lst)
    maxNum = max(lst)
    for i in range(minNum,maxNum+1):
        newlst.append(i)
    
    print len(newlst) - len(lst)
    
    
    
    
Consecutive([-2,10,4])