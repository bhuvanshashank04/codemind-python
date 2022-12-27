t,k=map(int,input().split())
a=list(map(int,input().split()))
cnt=0
for i in range(t):
    if a[i]%k!=0:
        cnt+=1
print(cnt)