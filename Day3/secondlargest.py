l=list(map(int,input().split()))
max=0
max2=0
for i in l:
    if i>max:
        max=i
for i in l:
	  if i>max2 and i!=max :
	       max2=i
print(max2)

