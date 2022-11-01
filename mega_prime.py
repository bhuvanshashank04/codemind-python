n=int(input())
s=str(n)
is_prime=True
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        is_prime=False
if is_prime==True:
    all_prime=True
    while n>0:
        r=n%10
        if r!=2 and r!=3 and r!=5 and r!=7:
            all_prime=False
        n=n//10
    if is_prime and all_prime:
        print('Mega Prime')
    else:
        print('Not Mega Prime')
else:
    print('Not Mega Prime')