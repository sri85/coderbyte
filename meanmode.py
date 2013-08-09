def MeanMode(lst):
    mean = sum(lst) / len(lst)
    
    mode =0
    
    for i in lst:
        if lst.count(i) >1:
            mode= i
        
    
    
    if (mode==mean):
        print 1
    else:
        print 0
    
MeanMode( [1, 2, 3])