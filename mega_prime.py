n=int(input())
is_prime=True
temp=str(n)
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        is_prime=False
if is_prime==True:
    cnt1=1
    while n>0:
        cnt=0
        r=n%10
        for j in range(1,r+1):
            if n%j==0:
                cnt+=1
        if cnt==2:
            cnt1+=1
        n=n//10
    if cnt1==len(temp):
        print('Mega Prime')
    else:
        print('Not Mega Prime')
else:
    print('Not Mega Prime')