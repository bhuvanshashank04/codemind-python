t=int(input())
a=list(map(int,input().split()))
s=0
for i in range(t):
    if a[i]%2!=0:
        break
    else:
        s+=a[i]
print(s)