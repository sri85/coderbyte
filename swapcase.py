def SwapCase(mystr):
    newStr =''
    for i in mystr:
        if i.isupper():
            newStr = newStr+ i.lower()
        else:
            newStr = newStr + i.upper()
    print newStr
   
   
SwapCase("Sup DUDE!!?")