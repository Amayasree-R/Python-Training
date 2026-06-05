l = list(map(int, input().split()))
k = int(input())

n = len(l)
k = k % n

l = l[-k:] + l[:-k]

print(l)