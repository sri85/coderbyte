def VowelCount(str):
    count = 0
    for ch in str:
        if(ch =='a' or ch =='e' or ch == 'i'or ch=='o' or ch =='u'):
            count = count+1
    print count

    
VowelCount("all cows eat grass")