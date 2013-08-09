#longest word
import math
def longestWord(str):
    print max(str.split(), key=len)

    
longestWord("i love dogs")