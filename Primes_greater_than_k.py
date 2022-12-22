t=int(input())
a=list(map(int,input().split()))
k=int(input())
cnt=0
for i in range(t):
    is_prime=True
    if a[i]==1:
        pass
    else:
        for j in range(2,int(a[i]**0.5)+1):
            if a[i]%j==0:
                is_prime=False
                break
        if is_prime==True and a[i]>=k:
            cnt+=1
print(cnt)