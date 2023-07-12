def rev(a):
    i=0
    j=len(a)-1
    while i<j:
        a[i],a[j]=a[j],a[i]
        i+=1
        j-=1
    return (a)
n,m=map(int,input().split())
a=[]
for i in range(n):
    r=list(map(int,input().split()))
    a.append(r)
c=0
for i in a:
    j=sorted(i)
    if i==j or i==rev(j):
        c+=1
print(c)