n=int(input())
rev=0
if n>=-231 and n<231:
    if n>0:
        while n>0:
            r=n%10
            if r!=0:
                rev=rev*10+r
            n=n//10
        print(rev)
    elif n<0:
        n=(-n)
        while n>0:
            r=n%10
            if r!=0:
                rev=rev*10+r
            n=n//10
        print(-rev)
else:
    print('0')