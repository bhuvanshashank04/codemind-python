t=int(input())
a=list(map(int,input().split()))
s=s1=0
for i in range(t//2):
    s+=a[i]
for i in range(t//2,t):
    s1+=a[i]
print(abs(s-s1))