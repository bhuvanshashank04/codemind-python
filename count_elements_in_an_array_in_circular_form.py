n=int(input())
a=list(map(int,input().split()))
for i in range(2):
    a.append(a[i])
cnt=0
for i in range(1,len(a)-1):
    if a[i-1]%2==0 and a[i+1]%2!=0 or a[i-1]%2!=0 and a[i+1]%2==0:
        cnt+=1
print(cnt)