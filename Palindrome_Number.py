t=int(input())
for _ in range(t):
    n=input()
    r=n[::-1]
    print(True) if n==r else print(False)