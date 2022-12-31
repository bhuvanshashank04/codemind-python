t=int(input())
a=list(map(int,input().split()))
cnt=0
for i in range(t):
    t=a[i]
    n=str(a[i])
    n=n[::-1]
    n=int(n)
    if n==t:
        cnt+=1
print(cnt)