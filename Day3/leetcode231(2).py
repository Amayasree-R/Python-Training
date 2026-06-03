l=list(map(int,input().split()))
mh=0
cnt=0
for i in range(0,len(l)):
    if l[i]>mh:
        mh=l[i]
        cnt=cnt+1
print(cnt)
