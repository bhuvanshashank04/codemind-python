t,k=map(int,input().split())
a=list(map(int,input().split()))
cnt=0
for i in range(t):
    if a[i]<0:
        a[i]=-a[i]
    n=str(a[i])
    if len(n)==k:
        cnt+=1
print(cnt)