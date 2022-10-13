n=int(input())
temp=n
sum=0
while n>0:
    pro=1
    r=n%10
    for i in range(r,0,-1):
        pro=pro*i
    sum+=pro
    n=n//10
if sum==temp:
    print('The number {} is a strong number'.format(sum))
else:
    print('The number {} is not a strong number'.format(temp))