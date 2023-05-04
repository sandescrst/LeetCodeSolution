def PalindromePerm(st):
    hMap = {}
    for i in st:
        if i in hMap:
            hMap[i] +=1
        else:
            hMap[i] = 1
    print(hMap)
    for k, v in hMap.items():
        oddFound = False
        if len(st)%2 ==0:
            if v%2 !=0: 
                return False
        
        else:
            if v%2 ==1:
                if oddFound:
                    return False
                oddFound= True
    return True     
        
print(PalindromePerm("tacocatt"))