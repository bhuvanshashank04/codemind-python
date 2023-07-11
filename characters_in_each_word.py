n=input()
cnt=0
for i in n:
    if i==' ':
        print(cnt,end=' ')
        cnt=0
    else:
        cnt+=1
print(cnt)