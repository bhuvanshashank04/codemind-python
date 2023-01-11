t=int(input())
for _ in range(t):
    n=int(input())
    pro=1
    for i in range(n,0,-1):
        pro*=i
    print(pro)