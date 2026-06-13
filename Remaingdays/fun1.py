def inr(n):
    if n==0:
        return
    print(n)
    inr(n-1)
n=5
inr(5)