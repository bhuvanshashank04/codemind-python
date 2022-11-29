t=int(input())
a=list(map(int,input().split()))
for i in range(t-1,-1,-1):
    if a[i]%2==0:
        print(a[i])
        break