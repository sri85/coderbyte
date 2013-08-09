def SecondGreatLow(lst):
    sortedList = sorted(lst)
    secondGreat = None
    secondLow = None
    if len(sortedList) >2 :
        
        if sortedList[0] == sortedList[1]:
            secondGreat = sortedList[2]
        else:
            secondGreat = sortedList[1]
    
    
        if sortedList[len(sortedList)-1] == sortedList[len(sortedList)-2]:
            secondLow = sortedList[len(sortedList)-3]
        else:
            secondLow = sortedList[len(sortedList)-2]
    
    
    
    else:
        secondGreat = sortedList[0]
        secondLow =   sortedList[1]
         
    print secondLow
    print secondGreat
SecondGreatLow( [7, 12, 7, 98, 106])
    