l=list(map(int,input().split()))
k=int(input())
n=len(l)
for j in range(k):
    last=l[n-1]
    for i in range(n-1,0,-1):
        l[i]=l[i-1]
    l[0]=last
print(l)
