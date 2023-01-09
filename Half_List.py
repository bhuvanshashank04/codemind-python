t=int(input())
a=list(map(int,input().split()))
for i in range(t-1,(t//2)-1,-1):
    print(a[i],end=' ')
for i in range(t//2):
    print(a[i],end=' ')