n=int(input())
while True:
    r=str(n)
    r=r[::-1]
    r=int(r)
    n+=r
    r=str(n)
    r=r[::-1]
    r=int(r)
    if r==n:
        break
print(n)