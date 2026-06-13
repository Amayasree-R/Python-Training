def dnr(n):
    if n==0:
        print("200")
        return
    print(n,end=" ")
    dnr(n-1)


n=5
dnr(n)

5 4 3 2 1 200
