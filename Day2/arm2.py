n=int(input())

n1=n


count=0
am=0
while n>0:
    count=count+1
    dig=n%10
    n=n//10

while n1>0:
    dig=n1%10
    am=am+dig**count
    count=count-1
    n1=n1//10

print(am)



