n=int(input())
vote=list(map(int,input().split()))
age=list(map(int,input().split()))
d={}
max1=0
maxkey=0
for i in range(n):
    if age[i]>=18:
            if vote[i] not in d:
                d[vote[i]]=1
            else:
                d[vote[i]]=d[vote[i]]+1
for i in d:
    if d[i]>max1:
        max1=d[i]
        maxkey=i
        count = 1
    elif d[i] == max1:
        count += 1

if count > 1:
    print("-1")
else:
    print(maxkey)

