t=int(input())
a=list(map(int,input().split()))
for i in range(t):
    if a[i]<0:
        n=str(a[i])
        print(len(n)-1,end=' ')
    else:
        n=str(a[i])
        print(len(n),end=' ')