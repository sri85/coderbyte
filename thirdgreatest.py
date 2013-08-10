def ThirdGreatest(strArr):
    wordlen =[]
    thirdGreat = 0
    result =[]
    for word in strArr:
        wordlen.append(len(word))
    print wordlen
    wordlen =  sorted(wordlen, key=int, reverse=True)
    
    thirdGreat = wordlen[2]
    
    for i in range(len(wordlen)):
        if len(strArr[i]) == thirdGreat:
            result.append(strArr[i])
    print result
    
    if len(result) > 1:
        print result[len(result)-1]
    else:
        print result[0]
    

ThirdGreatest([ "coder","byte","code"])