def fact(n):
    mul = 1
    for i in range(n,0,-1):
        mul = mul*i
    return mul

print(fact(5))