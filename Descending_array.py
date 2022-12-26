t=int(input())
a=list(map(int,input().split()))
cnt=0
for i in range(1,t):
    if a[i-1]>a[i]:
        pass
    else:
        cnt=1
        break
if cnt==0:
    print('yes')
else:
    print('no')