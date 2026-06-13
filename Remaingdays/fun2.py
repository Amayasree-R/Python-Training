def dnr(n):
    if n>5:
        return

    print(n)
    dnr(n+1)
n=1
dnr(n)