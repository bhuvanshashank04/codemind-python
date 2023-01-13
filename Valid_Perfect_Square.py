t=int(input())
for _ in range(t):
    a=int(input())
    root=a**0.5
    if root > int(root):
        print(False)
    else:
        print(True)