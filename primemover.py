def PrimeMover(n):
    primeArray =[]
    for num in range(1,10**4):
        prime = True
        for i in range(2,num):
            if (num%i==0):
                prime = False
        if prime:
            primeArray.append(num)
    print primeArray[n]

PrimeMover(16)