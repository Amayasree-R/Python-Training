n=int(input())
flag=0
if(n==0 or n==1):
    print("")
    exit()
else:
    for i in range(2,n//2+1): 
        if(n%i==0):
            flag=1
            break
if(flag==0):
    print("YES")
else:
    print("NO")