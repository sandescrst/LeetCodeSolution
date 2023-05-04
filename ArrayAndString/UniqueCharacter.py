def UniqueChar(st):
    for i in range(len(st)-1):
        for j in range(i+1,len(st)):
            if st[i] == st[j]:
                return False
            else:
                continue
    return True
    
print(UniqueChar("lambd"))