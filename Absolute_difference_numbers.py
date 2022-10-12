a,b=map(int,input().split())
n=a
num=rev=num1=num2=0
cnt1=cnt2=0
while n>0:
    if cnt1<b:
        r1=n%10
        cnt1+=1
        num=num*10+r1
        n=n//10
    else:
        temp=n
        n=0
while temp>0:
    r2=temp%10
    rev=rev*10+r2
    temp=temp//10
while rev>0:
    if cnt2<b:
        r3=rev%10
        cnt2+=1
        num1=num1*10+r3
        rev=rev//10
    else:
        rev=0
while num>0:
    rem=num%10
    num2=num2*10+rem
    num=num//10
if num2-num1>0:
    print(num2-num1)
else:
    print(-(num2-num1))