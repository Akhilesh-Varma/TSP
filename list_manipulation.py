def list_manip(x:list):
    return sum([i for i in x if i%2==0]*2)

print(list_manip([1,2,3,4,5]))