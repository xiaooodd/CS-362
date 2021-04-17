def divisors(n):
    if n == 0: return [0]
    if n == 1: return [1]
    rlist = []
    for i in range(1,n+1):
        if n%i == 0:
            rlist.append(i)

    return rlist
    
n = int(input("please enter an interge number:"))
print(divisors(n))
