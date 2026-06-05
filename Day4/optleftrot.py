

l=list(map(int,input().split()))
k=int(input())
n=len(l)
k=k%n
l=l[:k][::-1]+l[k:][::-1]
l=l[::-1]
print(l)
