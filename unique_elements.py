def unique(l):
    lst=[]
    for i in l:
        if i not in lst:
            lst.append(i)
    for i in lst:
        print(i,end=' ')
t=int(input())
a=list(map(int,input().split()))
unique(a)