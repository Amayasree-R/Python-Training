l=list(map(int,input().split()))
n=len(l)
p1=0
p2=n//2-1
for k in range(n//4):
    temp=l[p1]
    l[p1]=l[p2]
    l[p2]=temp
    p1=p1+1
    p2=p2-1
print(l)