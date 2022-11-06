h,m=map(int,input().split(':'))
h=h*30+m*0.5
m=m*6
ang=abs(h-m)
if 360-ang<ang:
    print(360-ang)
else:
    print(ang)