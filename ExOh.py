def ExOh(str):
    countX = 0
    countY = 0
    for ch in str:
        if ch =='x':
            countX = countX+1
        elif ch == 'o':
            countY = countY+1
    
    
    if countX == countY:
        print True
    else:
        print False
        

ExOh("xooxxo")