n,m=map(int,input().split())
a=[]
for i in range(n):
    r=list(map(int,input().split()))
    a.append(r)
s=0
for i in range(n):
    for j in range(m):
        if i==j:
           s+=a[i][j] 
j=m-1
for i in range(n):
    if i==j:
        j-=1
        continue
    s+=a[i][j]
    j-=1
print(s)