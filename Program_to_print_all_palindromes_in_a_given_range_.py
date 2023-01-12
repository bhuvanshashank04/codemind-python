a=int(input())
b=int(input())
for i in range(a,b+1):
    temp=i
    i=str(i)
    i=i[::-1]
    i=int(i)
    if i==temp:
        print(i,end=' ')