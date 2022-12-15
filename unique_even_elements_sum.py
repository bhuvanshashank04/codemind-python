t=int(input())
a=list(map(int,input().split()))
sum=0
s=set(a)
for i in s:
    if i%2==0:
        sum+=i
print(sum)