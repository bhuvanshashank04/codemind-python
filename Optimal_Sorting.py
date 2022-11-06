t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    cnt=0
    for i in range(n-1):
        if a[i]<a[i+1]:
            cnt+=1
    if cnt==n-1:
        print('0')
    else:
        print(max(a)-min(a))