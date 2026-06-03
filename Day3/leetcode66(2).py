for i in digits:
	sum=sum*10+i
sum=sum+1
res=[]
while(sum>0):
	rem=sum%10
	res.append(rem)
	sum=sum//10
res.reverse()
return res
	