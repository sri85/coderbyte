import decimal
import math
def DivisionStringified(num1,num2):
    result = None
    if num1/num2 > 9999:
        result ='{:20,.0f}'.format((num1) / (num2))
        print (result)
    else:
        print math.ceil(decimal.Decimal(num1) / decimal.Decimal(num2))
DivisionStringified(6874,67)