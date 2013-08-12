def PrimeTime(num):
    x = True 
    for i in range(2, num):
       if num%i == 0:
           x = False
           break 
       


    if x:
        print "true"
    else:
        print "false"

PrimeTime(2**16)    