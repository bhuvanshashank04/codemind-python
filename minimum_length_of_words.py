n=input()
n=n.split()
c=[]
for i in n:
    c.append(len(i))
print(min(c))