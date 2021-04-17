num = int(input("please enter an integer number:"))
root = math.ceil(math.sqrt(num))

divisor = []
for i in range(1,root+1):
    if num % i == 0:
        divisor.append(i)
print(divisor)
