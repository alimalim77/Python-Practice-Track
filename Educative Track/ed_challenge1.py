def foobar(mystr, pattern):
    pattern = sorted(pattern) 
    par = len(pattern)
    for i in range(0,len(mystr),1):
        print(sorted(mystr[i:i+par]))
        if sorted(mystr[i:i+par]) == pattern:
            return True
    return False
        
print(foobar("oidbcaf","abc"))