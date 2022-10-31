a=int(input())
b=int(input())
s=a+b+1
cnt=1
while True:
    is_prime=True
    for i in range(2,int(s**0.5)+1):
        if s%i==0:
            is_prime=False
            break
    if is_prime==True:
        print(cnt)
        break
    else:
        cnt+=1
        s+=1