def StringCompression(s):
    st = ""
    count =1
    i =0
    while (i < len(s)-1):
            if s[i]==s[i+1]:
                count+=1
                
            else:
                st += s[i]+ str(count)
                count =1
            i +=1   
            
    st = st+ s[-1] +str(count)
    return st
print(StringCompression("aabccccaaaddeer"))