l=list(map(int,input().split()))
k=int(input())
n=len(l)
s=sum(l[:k])
m=s
max=0
for i in range(1,n-k+1):
    s=s-l[i-1]+l[i+k-1]
    m=max(m,s)
print(m)
    
   