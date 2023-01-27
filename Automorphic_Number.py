n=int(input())
s=n**2
temp=n
cnt=c=rev=rev1=0
while temp>0:
    r=temp%10
    cnt+=1
    temp=temp//10
while s>0:
    if c<cnt:
        r1=s%10
        c+=1
        rev=rev*10+r1
        s=s//10
    else:
        s=0
while rev>0:
    r2=rev%10
    rev1=rev1*10+r2
    rev=rev//10
if rev1==n:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')