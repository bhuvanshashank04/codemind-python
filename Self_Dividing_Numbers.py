a=int(input())
b=int(input())
for i in range(a,b+1):
    cnt=cnt1=n=0
    temp=i
    while temp>0:
        r1=temp%10
        cnt1+=1
        temp=temp//10
    temp1=i
    temp2=i
    while i>0:
        r=i%10
        if r==0:
            n+=1
        elif temp1%r==0:
            cnt+=1
        i=i//10
    if cnt1==cnt:
        print(temp2,end=' ')