def add_n_numbers(*args):
    total_sum = 0
    for i in args:
        total_sum += i
    return total_sum

print(add_n_numbers(1,2,3,4,5))