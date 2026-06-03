l=list(map(int,input().split()))
k=int(input())
n=len(l)
for j in range(k):
    last=l[0]
    for i in range(0,n-1):
        l[i]=l[i+1]
    l[n-1]=last
print(l)



