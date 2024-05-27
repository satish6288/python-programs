def fibonacci_with_variable(n):
    res=[]
    a,b=0,1
    for _ in range(n):
        res.append(a)
        a,b=b,a+b
    return res




n = 10
result = fibonacci_with_variable(n)
print(result)

