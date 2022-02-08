def isPalindrome(s):
    return s == s[::-1]
arr=list(map(str, input().split(" ")))
arr1=[]
for i in arr:
    if(isPalindrome(i)):
        arr1.append(1)
    else:
        arr1.append(0)
        
i=0
sol=[]
while(i<len(arr1)):
    if(arr1[i]==1):
        vowel=[]
        cons=[]
        for ch in arr[i]:
            if (ch=="i"or ch=="I" or ch=="a" or ch=="A" or ch=="e" or ch=="E" or ch=="o" or ch=="O"or ch=="u"or ch=="U"):
                vowel.append(ch)
            else:
                cons.append(ch)
        
        pallinstr=""
        vowel.sort()
        for ch in vowel:
            pallinstr+=ch
        for ch in cons:
            pallinstr+=ch
        sol.append(pallinstr)
        
    else:
        vowel=[]
        cons=[]
        nonpall=""
        c=0;
        for ch in arr[i]:
            if ((c%2==0) and (ch=="i"or ch=="I"or ch=="a"or ch=="A"or ch=="e"or ch=="E"or ch=="o"or ch=="O"or ch=="u"or ch=="U")):
                vowel.append(ch)
            else:
                cons.append(ch)
            c+=1
        
        for ch in cons:
            nonpall+=ch
        for ch in vowel:
            nonpall+=ch
        sol.append(nonpall)
        
    i+=1
i=0
ans=[]
while(i<len(arr1)):
    if(arr1[i]==1):
        ans.append(sol[i])
    i+=1
i=0
while(i<len(arr1)):
    if(arr1[i]==0):
        ans.append(sol[i])
    i+=1
j=0
while(j<len(ans)):
    if(j<len(ans)-1):
        print(ans[j], end=",")
    else:
        print(ans[j])
    j+=1
   
                
                
