#number password generator
import random

def genpwd(num):
    a = pow(10, num-1)
    b = pow(10, num)-1
    return random.randint(a,b)
    
num = eval(input())
random.seed(17)
print(genpwd(num))