def dnr(n):
    if n==0:
        print("200")
        return
    dnr(n-1)
    print(n,end=" ")
    
    
    200 1 2 3 4 5
    