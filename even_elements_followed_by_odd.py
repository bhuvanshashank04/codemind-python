t=int(input())
a=list(map(int,input().split()))
for i in range(t):
    if a[i]%2==0:
        print(a[i],end=' ')
for j in range(t):
    if a[j]%2!=0:
        print(a[j],end=' ')