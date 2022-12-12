t=int(input())
a=list(map(int,input().split()))
cnt=0
for i in range(t):
    if a[i]==0:
        cnt+=1
    elif a[i]%2==0:
        cnt+=1
if cnt==t:
    print(True)
else:
    print(False)