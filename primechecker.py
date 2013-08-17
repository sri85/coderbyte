import itertools
def PrimeChecker(num):
    mylist = list(str(num))
    permlist= list(itertools.permutations(mylist))
    primelist=[]
    finalList =[]
    resultList =[]
    x = False
    
    for i in permlist:
        primelist.append( "".join(i))
    for i in primelist:
        finalList.append(int(i))
    print finalList
        
    for num in finalList:
        prime = True
        for i in range(2,num):
            
            if (num%i==0):
                
                prime =False
                
        if prime:
            resultList.append(num)
            
    if len(resultList) == 0:
        print 0
    else:
        print 1
                
    
    
    
            
PrimeChecker(22)