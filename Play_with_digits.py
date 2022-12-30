t=int(input())
a=list(map(int,input().split()))
s1=0
for i in range(t):
    s=0
    n=a[i]
    while n>0:
        r=n%10
        s+=r
        n=n//10
    s1+=s
print(s1)