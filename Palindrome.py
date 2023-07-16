def pali(n):
    n=str(n)
    return n==n[::-1]
n=int(input())
print(pali(n))