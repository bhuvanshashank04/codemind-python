n=int(input())
temp=n
cnt1=1
while cnt1>0:
    s=cnt=0
    while temp>0:
        r=temp%10
        cnt+=1
        temp=temp//10
    if cnt>1:
        while n>0:
            r1=n%10
            s+=r1
            n=n//10
        temp=s
        n=s
    elif cnt==1:
        cnt1=0
print(n)