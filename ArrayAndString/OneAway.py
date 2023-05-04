def OneAway(s1,s2):
    hMap = {}
    count =0
    for i in s1:
        if i in hMap:
            hMap[i] +=1
        else:
            hMap[i] = 1
    for i in s2:
        if i in hMap:
            if hMap[i] ==0:
                hMap[i] +=1
            else:
                hMap[i] -=1
        
    for k, v in hMap.items():
        count +=v

    print(hMap)
    print(count)
    return True if count <=1 else False

print(OneAway("pales", 'pale'))