import re
def NumberSearch(mystr):
    result = 0
    myList = []
    myList = re.findall(r'\d+', mystr)
    
    for i in myList:
        result = result + int(i)
    print result

NumberSearch("10 2One Number*1*")