n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a=set(a)
a=list(a)
b=set(b)
b=list(b)
cnt=0
for i in range(len(a)):
    if a[i] in b:
        cnt+=1
print(cnt)