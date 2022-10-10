n=int(input())
cnt=odd=even=0
while n>0:
    r=n%10
    cnt+=1
    n=n//10
    if r%2==0:
        even+=1
    elif r%2!=0:
        odd+=1
if cnt==even:
    print('Even')
elif cnt==odd:
    print('Odd')
else:
    print('Mixed')