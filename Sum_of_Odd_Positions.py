t=int(input())
a=list(map(int,input().split()))
s=0
for i in range(t):
    if i%2!=0:
        s+=a[i]
print(s)