#letterCapitalize

def letterCapitalize(str):
    split_str = list (str.split())
    new_str =[]
    
    for word in split_str:
        new_str.append( word.title())
        
    print " ".join(new_str)
        
letterCapitalize("hello world india")