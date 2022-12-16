t=int(input())
a=list(map(int,input().split()))
cnt=0
s=set(a)
for i in s:
    if i%2==0:
        cnt+=1
print(cnt)