def PermutationStep(num):
    numStr = str(num)
    mylist =[]
    finalNum = 0
    
    if(len(numStr)>3):
        firstTwo = numStr[0:2]
        for i in (numStr[2:]):
            mylist.append(i)
            mylist.sort(reverse= True)
    else:
        firstTwo = numStr[0:1]
        for i in (numStr[1:]):
            mylist.append(i)
            mylist.sort(reverse=True)
    
    
    
    finalNum=firstTwo+''.join(mylist)
    if(num == int(finalNum)):
        return -1
    else:
        return int(finalNum)
    
print PermutationStep(999)