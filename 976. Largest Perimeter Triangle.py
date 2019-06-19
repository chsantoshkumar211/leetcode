A=[2,1,1]
A.sort()
A=A[::-1]
f=0
for i in range(0,len(A)-2):
    a,b,c=A[i],A[i+1],A[i+2]
    if a+b>c and b+c>a and c+a>b:
        print(a+b+c)
        f=1
        break
if f==0:
    print(0)