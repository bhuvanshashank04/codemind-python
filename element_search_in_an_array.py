t=int(input())
a=list(map(int,input().split()))
n=int(input())
for i in range(t):
    if a[i]==n:
        print(True)
        i=-1
        break
if i!=-1:
    print(False)