def PermutationStep(num):
    numStr = str(num)
    mylist =[]
    
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
    
    
    print firstTwo
    print firstTwo+''.join(mylist)
    
    
PermutationStep(11121)