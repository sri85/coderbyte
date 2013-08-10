def DashInsert(num):
    lstNum = list(str(num))
    numArray = []
    firstNum  = int(lstNum[0])
    finalNum = ''
    for i in range(len(lstNum)-1):
        if(int(lstNum[i])%2!=0 and int(lstNum[i+1])%2!=0 ):
            numArray.append(-int(lstNum[i+1]))
        else:
            numArray.append(int(lstNum[i+1]))
    
    numArray.insert(0,(firstNum))
    for i in numArray:
        finalNum = finalNum + str(i)
    print (finalNum)
        
DashInsert(56730)