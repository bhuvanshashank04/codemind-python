a,b=map(int,input().split())
mul=a*b
while a!=0 and b!=0:
    if a>b:
        a%=b
    else:
        b%=a
if a==0:
    lcm=mul//b
else:
    lcm=mul//a
print(lcm)