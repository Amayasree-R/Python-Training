def dnr(n):
    if n<2:
        return

    print(n)
    dnr(n-2)
n=10
dnr(n)