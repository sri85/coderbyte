def RunLength(s):
    current = [s[0],1]
    
    result =''
    out = [current]
    for c in s[1:]:
        if c == current[0]:
            current[1] += 1
        else:
            current = [c, 1]
            out.append(current)
    #return out
    
    for i in out:
        for j in i:
            result = result + str(j)
    return result

print RunLength("wwwbbbw") 