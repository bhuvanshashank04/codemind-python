n=int(input())
rt=(n)**0.5
rt=int(rt)
cnt=0
for i in range(1,rt+1):
    if i**2==n:
        print(True)
        cnt=1
if cnt==0:
    print(False)