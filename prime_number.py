n=int(input())
is_prime=True
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        is_prime=False
if is_prime==True:
    print('prime')
else:
    print('not a prime')