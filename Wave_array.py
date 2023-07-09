n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(1,n-1):
    if a[i-1]<a[i] and a[i+1]<a[i]:
        pass
    elif a[i-1]>a[i] and a[i+1]>a[i]:
        pass
    else:
        c=1
if c==0:
    print('yes')
else:
    print('no')