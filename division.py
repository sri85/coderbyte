def  Division(num1,num2):
    gcdList = []
    for i in range(1,num2):
        if num1%i == 0 and num2%i ==0:
            gcdList.append(i)
    print max(gcdList)
Division(36,54)