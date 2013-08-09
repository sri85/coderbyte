#Letter Changes

def letterChanges(str):
    alphaList =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a"]
    split_str = list(str.lower())
    new_str =[]
    
    for x in range(0, len(split_str)):
        if(split_str[x].isalpha()):
            new_str.append(alphaList[(alphaList.index(split_str[x]))+1])
        else:
            new_str.append(split_str[x])
    print "".join(new_str).replace("a","A").replace("e","E").replace("i","I").replace("o","O").replace("u","U")
        
    
letterChanges("zdh#$")