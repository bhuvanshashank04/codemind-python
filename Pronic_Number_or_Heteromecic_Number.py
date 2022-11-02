n=int(input())
a=n//2
for i in range(1,a):
    c=i*(i+1)
    if n==c:
        print("YES")
        break
if n!=c:
    print("NO")