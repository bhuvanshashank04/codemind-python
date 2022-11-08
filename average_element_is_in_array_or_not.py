t=int(input())
a=list(map(int,input().split()))
avg=sum(a)//t
for i in range(t):
    if a[i]==avg:
        print(True)
        i=-1
        break
if i!=-1:
    print(False)