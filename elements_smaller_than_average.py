t=int(input())
a=list(map(int,input().split()))
avg=sum(a)//t
cnt=0
for i in range(t):
    if a[i]<=avg:
        cnt+=1
print(cnt)