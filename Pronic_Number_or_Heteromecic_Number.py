n=int(input())
temp=0
for i in range(1,n//2):
    if i*(i+1)==n:
        print('YES')
        temp=i
        i=(n//2)-1
if temp*(temp+1)!=n:
    print('NO')