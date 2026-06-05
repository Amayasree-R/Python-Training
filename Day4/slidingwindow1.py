l=list(map(int,input().split()))
k=int(input())
n=len(l)
sm=0
max=0
for i in range(0,n-k+1):
    s=l[i:i+k]
    sm=0
    for i in s:
        sm=sm+i
        if(sm>max):
            max=sm
            s1 = s[:]  #s1=s 
print(s1)
