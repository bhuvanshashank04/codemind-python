t=int(input())
a=list(map(int,input().split()))
s=cnt=0
for i in range(t):
    is_prime=True
    if a[i]==1:
        pass
    else:
        for j in range(2,int(a[i]**0.5)+1):
            if a[i]%j==0:
                is_prime=False
        if is_prime==True:
            cnt+=1
            s+=a[i]
avg=s/cnt
print('{:.2f}'.format(avg))