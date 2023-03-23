cid = [0,1,8,5,3,1,8,9]

def factorial(n):
    if n <= 1:
        return 1
    val = n * factorial(n-1)
    return val

def exd(i):
    S=0
    if i == 1:
        return (i**cid[5])/factorial(i-1)
    S += (i**cid[5])/factorial(i-1) + exd(i-1)
    return S
print(exd(15))