def fibo(t1,t2,n):
    if n==0:
        return t1
    elif n==1:
        return t2
    else:
        return(fibo(t1,t2,n-2)+fibo(t1,t2,n-1)**2)

t1, t2, n = [int(a) for a in input().split()]
res=fibo(t1,t2,n)
print(res)
