n=input()
a=list(n)
for i in range(len(a)):
    if a[i]=='6':
        a[i]='9'
        break
for i in a:
    print(i,end='')