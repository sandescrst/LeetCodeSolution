def PermutationWords(st1,st2):
    #Brute force
    st = max(st1, st2, key=len)
    stm = min(st1, st2, key=len)
    for i in stm:
        if i in st:
            continue
        else:
            return False
    return True

    
#ASCII method
def PermWords(st1,st2):
    a = 0
    for i in st1:
        a += ord(i)
    for i in st2:
        a -= ord(i)
    return a==0

# print(PermutationWords("hedfdlkflkdla", "hely"))
print(PermWords("dog", "god"))


