t=int(input())
a=list(map(int,input().split()))
for i in range(t):
    j=a[i]
    j=str(j)
    j=j[::-1]
    j=int(j)
    print(j,end=' ')