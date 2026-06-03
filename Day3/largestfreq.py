l=list(map(int,input().split()))
d={}
max1=0
cnt=0
maxkey=0
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
for i in d:
    if d[i]>max1:
        max1=d[i]
        maxkey=i
print(maxkey)


