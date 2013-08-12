def StringScramble(str1,str2):
    result = False
    for i in str2:
        if str1.count(i) ==0:
            result = False
            break
        else:
            result = True
    return result

print StringScramble("rkqodlw","world")