def occurence(stree):
    n = len(stree)
    for i in range(0,len(stree)) :
        count = 0
        for j in range((i+1),len(stree)):
            if(stree[i] == stree[j]):
                  temp = stree[i]                  
                  count+=1
        print(temp)
        print(count)
stree = string(input("Enter string"))        
occurence(stree)
