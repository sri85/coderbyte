#simpleSymbols
import re
def simpleSymbols(str):
    split_string = list(str)
    new_str =[]
    count =0
    for i in range(0,len(str)):
        if(split_string[split_string.index(""+str[i])-1]=="+" and split_string[split_string.index(""+str[i])+1]=="+"):
            new_str.append(True)
        

        if split_string[i].isalpha():
            count = count+1
    if count== len(new_str):
        print True
    else:
        print False

simpleSymbols("+d+=s=+s+")