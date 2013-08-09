def ArithGeo(lst):
    array1 =[]
    array2 =[]
    for i in range(len(lst)-1):
        array1.append(lst[i+1]-lst[i])
        array2.append(lst[i+1]/lst[i])
        
        
    def  checkEqual3(lst,lst1):
        if(lst[1:] == lst[:-1]):
            return "Arithmetic"

        if (lst1[1:] == lst1[:-1]):
            return "Geometric"
        else:
            return "-1"
    return checkEqual3(array1,array2)
print ArithGeo([1,2,3,4,6])