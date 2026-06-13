def dnr(n):
    if n==0:
        return

    print(n,end=" ")
    dnr(n-1)
    if n>1:

        print(n,end=" ")


n=10
dnr(n)

