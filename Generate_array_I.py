n=int(input())
a=list(map(int,input().split()))
for i in range(0,n,2):
    j=i+1
    while a[j]>0:
        print(a[i],end=' ')
        a[j]-=1