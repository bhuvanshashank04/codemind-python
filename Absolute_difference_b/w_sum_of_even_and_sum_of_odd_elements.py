t=int(input())
a=list(map(int,input().split()))
ev=od=0
for i in range(t):
    if a[i]%2==0:
        ev+=a[i]
    else:
        od+=a[i]
print(abs(ev-od))