def dnr(n):
   if n==1:
       return 0
   elif n%2==0:
       return 1+dnr(n/2)
   else:
       return 1+min(dnr(n-1),dnr(n+1))
n=15

print(dnr(n))



