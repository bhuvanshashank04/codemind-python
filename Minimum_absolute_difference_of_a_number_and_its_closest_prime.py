n=int(input())
n1=temp=n
cnt=0
for i in range(1,n+1):
    if n%i==0:
        cnt+=1
if cnt==2:
    print('0')
else:
    while True:
        is_prime=True
        for j in range(2,int(n**0.5)+1):
            if n%j==0:
                is_prime=False
                break
        if is_prime==True:
            p1=n
            break
        n+=1
    while True:
        prime=True
        for k in range(2,int(n1**0.5)+1):
            if n1%k==0:
                prime=False
                break
        if prime==True:
            p2=n1
            break
        n1-=1
    if abs(temp-p1)<abs(temp-p2):
        print(abs(temp-p1))
    else:
        print(abs(temp-p2))