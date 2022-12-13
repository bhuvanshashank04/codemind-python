t=int(input())
a=list(map(int,input().split()))
cnt=cnt1=0
for i in range(t):
    if a[i]%2!=0:
        cnt+=1
        if i%2!=0:
            cnt1+=1
if cnt==cnt1:
    print(True)
else:
    print(False)