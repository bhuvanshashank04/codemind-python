n=int(input())
a=list(map(int,input().split()))
cnt=0
for i in range(1,n-1,2):
    if a[i-1]<a[i] and a[i+1]<a[i]:
        cnt+=1
    elif a[i-1]>a[i] and a[i+1]>a[i]:
        cnt+=1
    else:
        print(-1)
        break
else:
    print(cnt)