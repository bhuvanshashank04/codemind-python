n=int(input())
a=list(map(int,input().split()))
s=sum(a)
while n>0:
    if s%n==0:
        print(n)
        break
    n-=1