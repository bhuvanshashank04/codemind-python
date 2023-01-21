a,b=map(int,input().split())
mx=a if a>b else b
i=mx
while True:
    if i%a==0 and i%b==0:
        print(i)
        break
    i+=mx