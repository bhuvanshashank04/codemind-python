t=int(input())
a=list(map(int,input().split()))
s=set(a)
sum=0
for i in s:
    if i%2!=0:
        sum+=i
print(sum)